#Requires -Version 5.1
<#
.SYNOPSIS
  Publish versioned PDF manuals with scp and sftp.
.DESCRIPTION
  Reads the connection from manuals.local.env next to this script. Checks the
  local PDFs and the remote names, then uploads only through a .uploading
  name and an sftp rename. -WhatIf checks and prints the plan. It does not
  upload. Existing remote files are never overwritten or deleted.
.PARAMETER Version
  Manual version to publish, for example 26.10 or 2026.10. Must match the
  five product conf.py files. Omit it to use those files.
.PARAMETER WhatIf
  Print the plan and check the remote names. Do not upload.
.PARAMETER Approval
  Must be exactly GO before an upload. -WhatIf does not need it.
#>
param(
    [string] $Version,

    [switch] $WhatIf,

    [string] $Approval
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$Manuals = @(
    @{ Project = 'eventreporter'; LocalName = 'EventReporter.pdf'; RemoteName = 'eventreporter-{0}.pdf' }
    @{ Project = 'mwagent'; LocalName = 'MonitorWareAgent.pdf'; RemoteName = 'monitorwareagent{0}.pdf' }
    @{ Project = 'rsyslog'; LocalName = 'RSyslogWindowsAgent.pdf'; RemoteName = 'rsyslogwindowsagent{0}.pdf' }
    @{ Project = 'winsyslog'; LocalName = 'WinSyslog.pdf'; RemoteName = 'winsyslog{0}.pdf' }
    @{ Project = 'winsyslog-j'; LocalName = 'WinSyslog-J.pdf'; RemoteName = 'winsyslog-j-{0}.pdf' }
)

$ConfProjects = @('eventreporter', 'mwagent', 'rsyslog', 'winsyslog', 'winsyslog-j')

function ConvertTo-ReleaseVersion {
    param([string] $VersionText)

    $text = $VersionText.Trim()
    if ($text -notmatch '^(?:(\d{4})|(\d{2}))\.(\d{1,2})$') {
        throw "Version must look like 26.10 or 2026.10. Got: $VersionText"
    }

    if ($Matches[1]) {
        $yy = [int] $Matches[1] % 100
    }
    else {
        $yy = [int] $Matches[2]
    }

    $month = [int] $Matches[3]
    if ($month -lt 1 -or $month -gt 12) {
        throw "Month must be 1-12. Got: $VersionText"
    }

    return [pscustomobject]@{
        Token = '{0}{1}' -f $yy, $month
        Label = '{0}.{1:D2}' -f $yy, $month
    }
}

function Format-ByteSize {
    param([long] $Bytes)
    return '{0:N1} MB' -f ($Bytes / 1MB)
}

function Assert-RemotePath {
    param([string] $Path)
    if ($Path -notmatch '^[A-Za-z0-9_./-]+$') {
        throw "Refusing remote path with unexpected characters: $Path"
    }
}

function Join-RemotePath {
    param([string] $Root, [string] $Child)
    $combined = $Root.TrimEnd('/') + '/' + $Child.TrimStart('/')
    Assert-RemotePath $combined
    return $combined
}

function Get-RepoRoot {
    $root = $PSScriptRoot
    for ($i = 0; $i -lt 3; $i++) {
        $root = Split-Path -Parent $root
    }
    if (-not (Test-Path -LiteralPath (Join-Path $root 'Makefile'))) {
        throw "Repository root not found from $PSScriptRoot"
    }
    return $root
}

function Read-LocalEnv {
    param([string] $Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Local env file is missing: $Path. Ask for MANUALS_SSH_TARGET, MANUALS_REMOTE_DIR, and MANUALS_TRANSPORT. Do not guess them."
    }

    $values = @{}
    $lineNumber = 0
    foreach ($line in Get-Content -LiteralPath $Path -Encoding UTF8) {
        $lineNumber++
        $trimmed = $line.Trim()
        if (-not $trimmed -or $trimmed.StartsWith('#')) { continue }
        if ($trimmed -notmatch '^([A-Za-z_][A-Za-z0-9_]*)=(.*)$') {
            throw "Cannot parse ${Path}:$lineNumber"
        }
        $values[$Matches[1]] = $Matches[2].Trim()
    }

    foreach ($name in @('MANUALS_SSH_TARGET', 'MANUALS_REMOTE_DIR', 'MANUALS_TRANSPORT')) {
        if (-not $values.ContainsKey($name) -or -not $values[$name]) {
            throw "Local env file is missing $name."
        }
    }

    $target = $values['MANUALS_SSH_TARGET']
    if ($target -notmatch '^[A-Za-z0-9._-]+@[A-Za-z0-9._-]+$') {
        throw 'MANUALS_SSH_TARGET has an unexpected form.'
    }
    if ($values['MANUALS_TRANSPORT'] -ne 'sftp') {
        throw "MANUALS_TRANSPORT must be sftp. Got: $($values['MANUALS_TRANSPORT'])"
    }
    Assert-RemotePath $values['MANUALS_REMOTE_DIR']

    return [pscustomobject]@{
        Target    = $target
        RemoteDir = $values['MANUALS_REMOTE_DIR']
    }
}

function Get-ConfiguredVersion {
    param([string] $RepoRoot)

    $labels = @()
    foreach ($project in $ConfProjects) {
        $path = Join-Path $RepoRoot "$project\conf.py"
        if (-not (Test-Path -LiteralPath $path)) {
            throw "Configuration not found: $path"
        }
        $text = Get-Content -LiteralPath $path -Raw -Encoding UTF8
        $found = [regex]::Matches($text, "(?m)^version\s*=\s*u?'([^']+)'")
        if ($found.Count -ne 1) {
            throw "Expected one version assignment in $path."
        }
        $labels += (ConvertTo-ReleaseVersion -VersionText $found[0].Groups[1].Value).Label
    }

    $unique = @($labels | Select-Object -Unique)
    if ($unique.Count -ne 1) {
        throw "Manual versions differ: $($labels -join ', ')."
    }
    return $unique[0]
}

function ConvertTo-NativeText {
    param($Output)

    $lines = foreach ($item in @($Output)) {
        if ($item -is [System.Management.Automation.ErrorRecord]) { $item.Exception.Message }
        else { "$item" }
    }
    return (($lines | Where-Object { $_ }) -join "`n").Trim() -replace "`r", ''
}

function Invoke-Sftp {
    param(
        [string] $Target,
        [string[]] $Commands
    )

    $batch = [System.IO.Path]::GetTempFileName()
    try {
        $content = (($Commands -join "`n") + "`n") -replace "`r", ''
        [System.IO.File]::WriteAllText($batch, $content, [System.Text.Encoding]::ASCII)
        $previous = $ErrorActionPreference
        $ErrorActionPreference = 'Continue'
        try {
            $output = & sftp.exe -o BatchMode=yes -o ConnectTimeout=30 -b $batch $Target 2>&1
            $code = $LASTEXITCODE
        }
        finally {
            $ErrorActionPreference = $previous
        }

        $text = ConvertTo-NativeText $output
        return [pscustomobject]@{
            ExitCode = $code
            Text     = $text
        }
    }
    finally {
        Remove-Item -LiteralPath $batch -Force -ErrorAction SilentlyContinue
    }
}

function Get-RemoteFileState {
    param(
        [string] $Target,
        [string] $RemotePath
    )

    Assert-RemotePath $RemotePath
    $result = Invoke-Sftp -Target $Target -Commands @("ls -l $RemotePath")
    if ($result.ExitCode -ne 0) {
        if ($result.Text -match 'not found|No such file') {
            return [pscustomobject]@{ Exists = $false; Size = 0L }
        }
        throw "sftp ls failed (exit $($result.ExitCode)) for ${RemotePath}: $($result.Text)"
    }

    foreach ($line in ($result.Text -split "`n")) {
        if ($line -match '(\d+)\s+[A-Z][a-z]{2}\s+\d+\s+(?:\d{4}|\d{1,2}:\d{2})\s+\S+\s*$') {
            return [pscustomobject]@{ Exists = $true; Size = [long] $Matches[1] }
        }
    }
    throw "No size in the sftp output for ${RemotePath}: $($result.Text)"
}

function Invoke-Scp {
    param(
        [string] $LocalPath,
        [string] $Target,
        [string] $RemotePath
    )

    Assert-RemotePath $RemotePath
    $destination = '{0}:{1}' -f $Target, $RemotePath
    $previous = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        & scp.exe -o BatchMode=yes -o ConnectTimeout=30 -- $LocalPath $destination
        $code = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previous
    }

    if ($code -ne 0) {
        throw "scp failed (exit $code): $LocalPath -> $destination"
    }
}

function Remove-UploadingFile {
    param(
        [string] $Target,
        [string] $RemotePath
    )

    $result = Invoke-Sftp -Target $Target -Commands @("rm $RemotePath")
    if ($result.ExitCode -ne 0) {
        throw "Could not remove ${RemotePath}: $($result.Text)"
    }
}

$repoRoot = Get-RepoRoot
$envPath = Join-Path $PSScriptRoot 'manuals.local.env'
$connection = Read-LocalEnv -Path $envPath
$configured = Get-ConfiguredVersion -RepoRoot $repoRoot

if ($Version) {
    $requested = ConvertTo-ReleaseVersion -VersionText $Version
    if ($requested.Label -ne $configured) {
        throw "Requested version $($requested.Label) does not match conf.py version $configured. Update the manuals with update-buildnumbers first."
    }
}
$release = ConvertTo-ReleaseVersion -VersionText $configured

$files = @()
$missing = @()
foreach ($manual in $Manuals) {
    $localPath = Join-Path $repoRoot (Join-Path "build\pdf\$($manual.Project)" $manual.LocalName)
    $publicName = $manual.RemoteName -f $release.Token
    if ($publicName -notmatch '^[A-Za-z0-9.-]+\.pdf$') {
        throw "Unexpected public manual name '$publicName'."
    }
    $remotePath = Join-RemotePath $connection.RemoteDir $publicName
    $uploadingPath = Join-RemotePath $connection.RemoteDir ($publicName + '.uploading')
    $files += [pscustomobject]@{
        Project        = $manual.Project
        PublicName     = $publicName
        LocalPath      = $localPath
        RemotePath     = $remotePath
        UploadingPath  = $uploadingPath
    }
    if (-not (Test-Path -LiteralPath $localPath)) {
        $missing += $localPath
        continue
    }
    $length = (Get-Item -LiteralPath $localPath).Length
    if ($length -le 0) {
        $missing += "$localPath (empty)"
    }
}

Write-Host ""
Write-Host "Release: $($release.Label)"
Write-Host "Token: $($release.Token)"
Write-Host "Ziel: $($connection.Target):$($connection.RemoteDir)"
Write-Host "Transport: scp und sftp"
Write-Host ""

if ($missing.Count -gt 0) {
    Write-Host "Lokale PDF-Dateien fehlen. Remote wurde nichts geaendert."
    foreach ($path in $missing) { Write-Host "  $path" }
    exit 1
}

if (-not $WhatIf -and $Approval -cne 'GO') {
    Write-Host "STOP. Upload braucht exakt -Approval GO. Remote wurde nichts geaendert."
    exit 1
}

Write-Host "Upload:"
foreach ($file in $files) {
    $item = Get-Item -LiteralPath $file.LocalPath
    Write-Host ('    {0,-32} {1,10}  {2}' -f $file.PublicName, (Format-ByteSize $item.Length), $file.LocalPath)
}
Write-Host ""

$problems = @()
foreach ($file in $files) {
    $finalState = Get-RemoteFileState -Target $connection.Target -RemotePath $file.RemotePath
    $uploadState = Get-RemoteFileState -Target $connection.Target -RemotePath $file.UploadingPath
    if ($finalState.Exists) {
        $problems += "$($file.RemotePath) existiert bereits ($($finalState.Size) Bytes) und wird nicht ueberschrieben."
    }
    if ($uploadState.Exists) {
        $problems += "$($file.UploadingPath) existiert bereits ($($uploadState.Size) Bytes). Remote wurde nichts ersetzt."
    }
}

if ($problems.Count -gt 0) {
    Write-Host "STOP. Remote wurde nichts geaendert."
    foreach ($problem in $problems) { Write-Host "  $problem" }
    exit 1
}

Write-Host "Remote-Status: die fuenf Zieldateien sind frei."
if ($WhatIf) {
    Write-Host "VORSCHAU. Es wurde nichts veraendert."
    exit 0
}

function Publish-ManualFile {
    param($File)

    $localSize = (Get-Item -LiteralPath $File.LocalPath).Length
    $finalState = Get-RemoteFileState -Target $connection.Target -RemotePath $File.RemotePath
    $uploadState = Get-RemoteFileState -Target $connection.Target -RemotePath $File.UploadingPath
    if ($finalState.Exists -or $uploadState.Exists) {
        throw "STOP. $($File.PublicName) oder die .uploading-Datei ist inzwischen vorhanden. Nichts ueberschrieben."
    }

    try {
        Invoke-Scp -LocalPath $File.LocalPath -Target $connection.Target -RemotePath $File.UploadingPath
    }
    catch {
        $scpError = $_
        try {
            $leftover = Get-RemoteFileState -Target $connection.Target -RemotePath $File.UploadingPath
            if ($leftover.Exists) {
                Remove-UploadingFile -Target $connection.Target -RemotePath $File.UploadingPath
            }
        }
        catch {
            Write-Host "Konnte $($File.UploadingPath) nach fehlgeschlagenem scp nicht entfernen: $($_.Exception.Message)"
        }
        throw $scpError
    }
    $uploaded = Get-RemoteFileState -Target $connection.Target -RemotePath $File.UploadingPath
    if (-not $uploaded.Exists -or $uploaded.Size -ne $localSize) {
        if ($uploaded.Exists) {
            Remove-UploadingFile -Target $connection.Target -RemotePath $File.UploadingPath
        }
        $remoteSize = $(if ($uploaded.Exists) { $uploaded.Size } else { 'missing' })
        throw "Groesse stimmt nicht fuer $($File.UploadingPath): lokal $localSize, remote $remoteSize. Die .uploading-Datei wurde entfernt."
    }

    $finalAgain = Get-RemoteFileState -Target $connection.Target -RemotePath $File.RemotePath
    if ($finalAgain.Exists) {
        Remove-UploadingFile -Target $connection.Target -RemotePath $File.UploadingPath
        throw "STOP. $($File.RemotePath) ist inzwischen vorhanden. Die .uploading-Datei wurde entfernt und der vorhandene Name nicht angetastet."
    }

    $renamed = Invoke-Sftp -Target $connection.Target -Commands @("rename $($File.UploadingPath) $($File.RemotePath)")
    if ($renamed.ExitCode -ne 0) {
        $stageLeft = Get-RemoteFileState -Target $connection.Target -RemotePath $File.UploadingPath
        $publishedNow = Get-RemoteFileState -Target $connection.Target -RemotePath $File.RemotePath
        $renameLanded = $publishedNow.Exists -and $publishedNow.Size -eq $localSize -and -not $stageLeft.Exists
        if ($stageLeft.Exists) {
            Remove-UploadingFile -Target $connection.Target -RemotePath $File.UploadingPath
        }
        if (-not $renameLanded) {
            throw "sftp rename failed (exit $($renamed.ExitCode)): $($File.UploadingPath) -> $($File.RemotePath). $($renamed.Text)"
        }
        Write-Host "sftp rename meldete Exit $($renamed.ExitCode), die Zieldatei hat aber die richtige Groesse."
    }

    $published = Get-RemoteFileState -Target $connection.Target -RemotePath $File.RemotePath
    if (-not $published.Exists -or $published.Size -ne $localSize) {
        throw "Groesse stimmt nicht fuer $($File.RemotePath) nach dem Umbenennen: lokal $localSize, remote $($published.Size)."
    }

    $chmod = Invoke-Sftp -Target $connection.Target -Commands @("chmod 644 $($File.RemotePath)")
    if ($chmod.ExitCode -ne 0) {
        Write-Host "chmod 644 fuer $($File.RemotePath) nicht gesetzt: $($chmod.Text)"
    }
    Write-Host "$($File.PublicName) $($published.Size) Bytes"
}

Write-Host ""
Write-Host "Upload startet."
foreach ($file in $files) {
    Publish-ManualFile -File $file
}

Write-Host ""
Write-Host "Fertig. Release $($release.Label) ist hochgeladen."
exit 0
