:orphan:

.. _event-id-procedure-file-diagnose-log-rotation:

.. meta::
   :description: Verify trigger, names, handles, destination access, and retention.
   :procedure-id: file.diagnose-log-rotation
   :procedure-reference: true

Diagnose log rotation and retention
===================================

When to use this procedure
--------------------------

Use when files do not rotate or retention cannot rename/delete eligible files.

Applies to
----------

This procedure applies to WinSyslog.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Run diagnostic checks before changing configuration.
- Remove passwords, private keys, license data, and other secrets from evidence.

Configuration path
------------------

Configuration Client > the service, rule, or action named on the Event ID page.

Procedure
---------

#. Record active path, trigger, naming pattern, and retention settings.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-ChildItem -LiteralPath '<LOG_DIRECTORY>' | Sort-Object LastWriteTime | Format-Table Name,Length,LastWriteTime
      Get-Acl -LiteralPath '<LOG_DIRECTORY>' | Format-List AccessToString

   **Expected result:** A controlled rotation creates the expected file, active output continues, and only eligible files are removed.

   **If it fails:** Correct ACLs, naming conflicts, timing, free space, or external handle interference.

#. Perform one uniquely identifiable product test through the same service, rule, or action.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output; do not change unrelated settings.

Verify the result
-----------------

Repeat the affected operation, confirm its positive output, and verify that queues, collection positions, or remote delivery continue normally.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- The command output, relevant configuration export, and bounded debug log from the same interval.

Related Event IDs
-----------------

- :ref:`WinSyslog Event ID 11026 <winsyslog-event-id-11026>`
- :ref:`WinSyslog Event ID 11153 <winsyslog-event-id-11153>`
- :ref:`WinSyslog Event ID 11154 <winsyslog-event-id-11154>`
- :ref:`WinSyslog Event ID 11155 <winsyslog-event-id-11155>`
- :ref:`WinSyslog Event ID 11156 <winsyslog-event-id-11156>`
- :ref:`WinSyslog Event ID 11157 <winsyslog-event-id-11157>`
- :ref:`WinSyslog Event ID 11158 <winsyslog-event-id-11158>`
- :ref:`WinSyslog Event ID 11159 <winsyslog-event-id-11159>`
- :ref:`WinSyslog Event ID 11160 <winsyslog-event-id-11160>`
- :ref:`WinSyslog Event ID 11161 <winsyslog-event-id-11161>`
- :ref:`WinSyslog Event ID 11162 <winsyslog-event-id-11162>`
- :ref:`WinSyslog Event ID 11163 <winsyslog-event-id-11163>`
- :ref:`WinSyslog Event ID 11183 <winsyslog-event-id-11183>`
- :ref:`WinSyslog Event ID 11222 <winsyslog-event-id-11222>`


Related procedures
------------------

- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>`
