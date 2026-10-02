---
name: rebuild-chm
description: Rebuild this repository's six HTML Help manuals by generating HTMLHelp sources in WSL and compiling the CHM files with Windows HTML Help Workshop.
---

# Rebuild CHM manuals with WSL and Windows

Use this skill when asked to rebuild or regenerate the `.chm` help files in
this documentation repository.

## Build layout

The six Sphinx projects are `eventreporter`, `mwagent`, `rsyslog`,
`syslogviewer`, `winsyslog`, and `winsyslog-j`. `make all-htmlhelp` generates
their HTMLHelp source trees under `build/chm/<project>/`. The Windows HTML Help
Compiler (`hhc.exe`) compiles each `.hhp` project file into a `.chm` alongside
that source tree. Final CHM files belong in `build/`. The English and Japanese
WinSyslog projects both configure the basename `WinSyslog.chm`; preserve both
outputs by naming the Japanese root copy `WinSyslog-J.chm`.

When the sibling checkout `../adiscon-client` is present, five of the CHMs are
copied to product output folders expected by its build. SyslogViewer has no
corresponding destination there. The CHMs can still be built without the
sibling checkout; in that case, the script warns and skips those five copies.

The repository's `build-chm.bat` supports both a full Windows build and a
`--compile-only` mode. The full build requires the Windows virtual environment
(`venv/Scripts/python.exe`). After building HTMLHelp sources in WSL, use
`--compile-only` from Windows to compile with `hhc.exe` and copy the outputs
without rebuilding the sources.

## Workflow

1. Inspect the working tree and preserve existing user changes. In WSL, find
   the checkout root and its corresponding Windows path rather than assuming
   a fixed checkout location:

   ```bash
   repo_root="$(git rev-parse --show-toplevel)"
   repo_windows="$(wslpath -w "$repo_root")"
   printf 'WSL checkout: %s\nWindows checkout: %s\n' "$repo_root" "$repo_windows"
   ```

   `wslpath -w` returns the Windows drive path for a mounted Windows checkout,
   or the `\\wsl.localhost\...` path when the checkout is in the WSL
   filesystem. The Windows compiler must use this Windows path to reach the
   `.hhp` files. If you need the five client copies, confirm that the sibling
   `../adiscon-client` checkout exists.
2. In WSL, activate the repository's Linux virtual environment and build all
   HTMLHelp sources with strict Sphinx warnings:

   ```bash
   source "$repo_root/venv/bin/activate"
   make -C "$repo_root" all-htmlhelp SPHINXOPTS="-W --keep-going"
   ```

   If the virtual environment is missing, follow the repository's setup
   instructions. Do not try to use the Windows virtual environment from WSL.
3. Confirm that Windows HTML Help Workshop is available to `build-chm.bat`
   through `$env:HHC`, its standard install location, or `PATH`. Stop and
   report if `hhc.exe` is unavailable; do not install software without the
   user's request.
4. From Windows PowerShell, use the Windows checkout path printed in step 1
   to run the compiler/copy phase against the WSL-built sources:

   ```powershell
   $repo = '<Windows checkout path printed in WSL>'
   & "$repo\build-chm.bat" --compile-only
   ```

   The script compiles the `.hhp` files with Windows `hhc.exe`, copies six
   distinct CHMs into the repository's `build/`, and, when the sibling client
   checkout exists, copies the five required manuals there. It names the
   Japanese WinSyslog CHM `WinSyslog-J.chm` in `build/` to avoid a collision
   with the English file. If the sibling checkout is absent, expect a warning
   and verify only the six repository outputs.
5. Verify that all six distinct CHMs exist in this repository's `build/`
   directory. If the sibling client checkout is present, also verify that the
   script copied these five files and that each destination matches its
   source size:

   | Project | Destination relative to `../adiscon-client` |
   |---|---|
   | EventReporter | `CFGEvntSLog/bin/Release/manual/EventReporter.chm` |
   | MonitorWare Agent | `MWAgent/bin/Release/manual/MonitorWareAgent.chm` |
   | RSyslog Windows Agent | `RSyslogConfigClient/bin/Release/manual/RSyslogWindowsAgent.chm` |
   | WinSyslog | `WINSyslogClient/bin/Release/manual/WinSyslog.chm` |
   | WinSyslog Japanese | `WINSyslogClient/bin/Release.JP/manual/WinSyslog.chm` |

   Do not copy the SyslogViewer CHM into the client repository. If the sibling
   checkout is absent, expect a warning and skip checking these five client
   destinations. Do not treat `hhc.exe`'s exit code alone as proof of success.
6. Report the WSL Sphinx result, Windows compiler result, and all six files
   under `build/`. When the sibling checkout is present, also report the five
   client destinations; otherwise report that those copies were skipped
   because the checkout was absent. Do not commit, tag, push, or publish the
   generated files.

If WSL cannot start or cannot access the checkout, stop and report the exact
error. Do not restart WSL services or change Windows/WSL configuration. If the
user wants an all-Windows build instead, run `build-chm.bat` without
`--compile-only` from PowerShell or Command Prompt; it performs the Sphinx
build itself and requires the Windows virtual environment.
