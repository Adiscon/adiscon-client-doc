.. _rsyslogwa-tour-operate-and-troubleshoot:

Operate and Troubleshoot
========================

After initial setup, most operational work is validating event intake, tuning
rules, and diagnosing why forwarding succeeded, failed, or behaved differently
than expected.

Quick checklist
---------------

1. Confirm the rsyslog Windows Agent service is running.
2. Confirm the collection service is enabled and bound to the intended ruleset.
3. Confirm your rule order and filters match what you expect.
4. Check the forwarding action host, port, and transport settings.

Useful diagnostics
------------------

- Export the current configuration and collect a debug log when investigating
  problems. See :doc:`tutorial-export-config-and-debug-log`.
- If forwarding to rsyslog fails, verify connectivity, protocol mode, TLS or
  certificate settings, and receiver-side listener configuration.

Where to look next
------------------

- Input issues: :doc:`Services <services>`
- Matching issues: :doc:`Filter Conditions <filterconditions>`
- Output issues: :doc:`Actions <actions>`
- Common operational questions: :doc:`faq`
