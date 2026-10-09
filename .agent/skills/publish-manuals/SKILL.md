---
name: publish-manuals
description: >-
  Builds the product PDF manuals and uploads each one under its versioned
  public file name. Use when the user asks to publish, upload, or release the
  PDF manuals. Connection settings come from the local env file.
disable-model-invocation: true
---

# Publish PDF manuals

Use this skill when the finished PDF manuals should be published. Do not upload
during an ordinary documentation edit, a version bump, or a CHM rebuild.

The upload script is [Publish-Manuals.ps1](Publish-Manuals.ps1). It reads the
connection from `manuals.local.env` in this directory. That file is gitignored.
Do not copy its values into this skill, the script, a commit, or any other
tracked file. If the file or one of its variables is missing, stop and ask the
user. Do not guess a host or a remote directory.

`MANUALS_TRANSPORT` must be `sftp`. The script then uses only `scp` and `sftp`.
Do not call `ssh` with a remote command. Do not put passwords in the command.

## Manuals

Build and upload these five manuals. `winsyslog` is the English manual.
`winsyslog-j` is the Japanese manual, a separate Sphinx project and a separate
PDF. Do not upload SyslogViewer or older products that are not in this list.

| Project | Local PDF | Public file |
| --- | --- | --- |
| eventreporter | `build/pdf/eventreporter/EventReporter.pdf` | `eventreporter-<token>.pdf` |
| mwagent | `build/pdf/mwagent/MonitorWareAgent.pdf` | `monitorwareagent<token>.pdf` |
| rsyslog | `build/pdf/rsyslog/RSyslogWindowsAgent.pdf` | `rsyslogwindowsagent<token>.pdf` |
| winsyslog | `build/pdf/winsyslog/WinSyslog.pdf` | `winsyslog<token>.pdf` |
| winsyslog-j | `build/pdf/winsyslog-j/WinSyslog-J.pdf` | `winsyslog-j-<token>.pdf` |

Keep those public names. The 26.x files already on the server do not all use a
hyphen, and EventReporter does. Do not rename an existing remote file and do
not upload an unversioned name.

## Version token

Read `version` from these five files. All five must be identical:

- `eventreporter/conf.py`
- `mwagent/conf.py`
- `rsyslog/conf.py`
- `winsyslog/conf.py`
- `winsyslog-j/conf.py`

Accept `26.10` or `2026.10`. Drop the dot and any leading zero on the month:
`26.09` becomes `269`, and `26.10` becomes `2610`. If the user names a version,
it must match the five configuration files. Otherwise stop and point to
[update-buildnumbers](../update-buildnumbers/SKILL.md). Do not guess.

## Build

Before building final release PDFs, complete the
[release-manual content checklist](../../../AGENTS.md#414-release-manual-content-checklist).
Update in-scope scheduled availability and approved errata in the sources,
then build from those updated sources. A version bump or ordinary rebuild
alone does not establish product release or erratum publication approval.

In WSL, find the checkout and build only the five manuals. Use the Linux
virtual environment. Do not build from the Windows virtual environment inside
WSL.

```bash
repo_root="$(git rev-parse --show-toplevel)"
source "$repo_root/venv/bin/activate"
make -C "$repo_root" pdf-eventreporter pdf-mwagent pdf-rsyslog pdf-winsyslog pdf-winsyslog-j SPHINXOPTS="-W"
```

If the build fails, stop. Do not upload a partial set. Leave the Sphinx output
names unchanged. The script copies each PDF to its public name only as the
upload source.

## GO gate

Do not upload until the user replies with exactly `GO`.

1. Run the preview from the repository root:

```powershell
.\.agent\skills\publish-manuals\Publish-Manuals.ps1 -WhatIf
```

Pass `-Version` only when the user named one and it matches the configuration
files.

2. If the preview exits non-zero, show the error and stop. Do not ask for GO.
3. If the preview succeeds, show its output unchanged. Then stop and wait.
4. Run the upload only after the user's next message is exactly `GO`
   (trimmed). `ok`, `ja`, `yes`, and `go` are not approval. The script itself
   rejects the upload unless `-Approval GO` is present:

```powershell
.\.agent\skills\publish-manuals\Publish-Manuals.ps1 -Approval GO
```

   Pass the same `-Version` used for the preview.
5. Show the script result. On an existing remote file or a size mismatch, stop
   and report the path. Do not retry, delete, or overwrite unless the user
   asks.

The script refuses when the public name or a leftover `.uploading` file
already exists. It uploads to `<name>.pdf.uploading`, checks the size, and
renames only when the size matches. If `scp` or the rename fails and the
public file was not created, it removes that `.uploading` file and stops. It
never copies directly onto the public name and never deletes a public file.

## Out of scope

- Do not commit, tag, or push the generated PDFs or `manuals.local.env`.
- Do not commit this skill's local env file if it appears in `git status`.
- HTML, CHM, and the product websites that link to the PDFs stay unchanged.
