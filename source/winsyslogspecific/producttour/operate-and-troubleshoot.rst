.. _winsyslog-tour-operate-and-troubleshoot:

Operate and Troubleshoot
========================

After initial setup, most operational work is validating inputs, tuning rules,
and diagnosing why something did or did not happen.

Quick checklist
---------------

1. Confirm the WinSyslog service is running (Windows Services / `services.msc`).
2. Confirm your input service is enabled and attached to the intended ruleset.
3. Confirm your rule order and filters match what you expect.
4. Add a temporary :doc:`Write to File <../../mwagentspecific/a-fileoptions>` action to see raw output quickly.

Testing tools
-------------

- To validate syslog reception, use the WinSyslog Configuration Client menu `Tools`
  and run `Send Syslog Test Message` (see :ref:`Send Syslog Test Message <winsyslog-send-test-message>`).

Where to look next
------------------

- Input issues: :doc:`Services <../services>`
- Matching issues: :doc:`Filter conditions <../filterconditions>`
- Output issues: :doc:`Actions <../actions>`
- UI basics and defaults vs. instances: :ref:`winsyslog-configuring`
