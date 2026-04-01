<#
.SYNOPSIS
Creates the WinSyslogDemo ODBC System DSN for the WinSyslog quick start.

.DESCRIPTION
Run this script in an elevated PowerShell session on the WinSyslog host.
It creates or replaces a System DSN by using the built-in WDAC ODBC cmdlets.

The script keeps credentials out of the DSN. Use -UseTrustedConnection only if
you want the DSN itself to use Windows authentication for connection tests.
#>

[CmdletBinding()]
param(
    [string]$Name = 'WinSyslogDemo',
    [string]$Server = 'localhost',
    [string]$Database = 'WinSyslogDemo',
    [string]$DriverName = 'ODBC Driver 18 for SQL Server',
    [ValidateSet('32-bit', '64-bit')]
    [string]$Platform = '64-bit',
    [switch]$UseTrustedConnection
)

$dsnProperties = @(
    "Server=$Server",
    "Database=$Database"
)

if ($UseTrustedConnection) {
    $dsnProperties += 'Trusted_Connection=Yes'
    $dsnProperties += 'TrustServerCertificate=Yes'
}

$existingDsn = Get-OdbcDsn -Name $Name -DsnType System -Platform $Platform -ErrorAction SilentlyContinue
if ($null -ne $existingDsn) {
    $existingDsn | Remove-OdbcDsn -ErrorAction Stop
}

Add-OdbcDsn -Name $Name `
    -DriverName $DriverName `
    -DsnType System `
    -Platform $Platform `
    -SetPropertyValue $dsnProperties `
    -PassThru `
    -ErrorAction Stop | Out-Null

Write-Host "Created System DSN '$Name' on $Platform with driver '$DriverName'."
Write-Host "Open Data Sources (ODBC), test the DSN, and then select it in WinSyslog."
