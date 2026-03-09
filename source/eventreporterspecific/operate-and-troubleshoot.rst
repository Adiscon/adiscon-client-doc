.. _eventreporter-tour-operate-and-troubleshoot:

Operate and Troubleshoot
========================

After initial setup, most operational work is validating event intake, tuning
rules, and diagnosing why something did or did not happen.

Quick checklist
---------------

1. Confirm the EventReporter service is running.
2. Confirm the Event Log Monitor service is enabled and bound to the intended
   ruleset.
3. Confirm your rule order and filters match what you expect.
4. Add a temporary :doc:`Write to File <../mwagentspecific/a-fileoptions>`
   action to inspect raw output quickly.

Useful diagnostics
------------------

- Export the current configuration and collect a debug log when investigating
  problems. See :doc:`tutorial-export-config-and-debug-log`.
- If output to a remote system fails, verify connectivity, protocol settings,
  and credentials on both sides.

Where to look next
------------------

- Input issues: :doc:`Services <services>`
- Matching issues: :doc:`Filter Conditions <filterconditions>`
- Output issues: :doc:`Actions <actions>`
- Common operational questions: :doc:`faq`
