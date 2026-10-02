---
name: update-buildnumbers
description: Update the synchronized Sphinx manual versions for this documentation repository when preparing a documentation release.
---

# Update documentation versions

Use this skill when asked to update, bump, or align the documented release
versions for this repository.

## Version format and scope

This repository stores the manual version as `YY.MM` in each product's
`conf.py`. It does not store a per-build counter or a fourth version component.
Do not invent or increment a build number here. If the request explicitly
requires an actual product build number, explain that it is maintained in the
product repository; do not change these manual versions as a substitute.

The six manual configurations are:

| Manual | Configuration |
|---|---|
| EventReporter | `eventreporter/conf.py` |
| MonitorWare Agent | `mwagent/conf.py` |
| rsyslog | `rsyslog/conf.py` |
| SyslogViewer | `syslogviewer/conf.py` |
| WinSyslog | `winsyslog/conf.py` |
| WinSyslog Japanese | `winsyslog-j/conf.py` |

Each file defines both `version` and `release`. Keep those values identical
within the file, and keep all six manuals aligned unless the user explicitly
requests a narrower scope. WinSyslog and WinSyslog Japanese must stay in
version parity.

## Workflow

1. Inspect the working tree and read the `version` and `release` values from
   all six configuration files. Preserve unrelated user changes.
2. Determine the target `YY.MM`. Use the user's explicit target when provided;
   otherwise use the current calendar month, with a two-digit year and a
   zero-padded two-digit month (for example, October 2026 is `26.10`). The
   invocation of this skill authorizes aligning all six manuals to that
   current-month version, so do not ask for confirmation solely because the
   user omitted a target. If the user specifies a release date or version that
   conflicts with the current month, use the user's explicit target.
3. Update the `version` and `release` assignments in the requested
   configuration files. Unless the user requests a narrower scope, update all
   six. If either WinSyslog manual is in scope, include both English and
   Japanese manuals so they remain in parity. These values also feed the
   generated Event ID references, so regenerate those outputs after changing
   the configurations:

   ```bash
   python3 scripts/generate_event_id_reference.py
   python3 scripts/generate_event_id_reference.py --check
   ```

   The generator updates the product version recorded in the generated Event
   ID JSON and `llms.txt` files under `source/_generated/event-ids/`. Include
   those generated changes when they are produced by the version update. Do
   not edit product source versions, release notes, or unrelated files.
4. Verify that each requested config has matching `version` and `release`
   values equal to the target. When the default all-manual scope applies, also
   verify all six manuals agree. Always verify that the English and Japanese
   WinSyslog versions agree, even when neither is being changed. Confirm the
   generator's `--check` succeeds, review the scoped diff, and run
   `git diff --check`.
5. Report the previous and new manual version and list the files changed. Do
   not commit, tag, push, or publish unless separately requested.

If the user asks only to "increment the build number" without invoking this
skill or asking to update the manuals, explain that this repository has no
build-number field and ask whether they want the manuals aligned to the current
month. If the user invokes this skill, use the current-month rule above.
