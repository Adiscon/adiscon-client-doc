:orphan:

.. _event-id-procedure-filemonitor-verify-source-state-and-encoding:

.. meta::
   :description: Check source path, sharing, encoding, line endings, and read position.
   :procedure-id: filemonitor.verify-source-state-and-encoding
   :procedure-reference: true

Verify File Monitor source state and encoding
=============================================

When to use this procedure
--------------------------

Use for File Monitor startup, read, conversion, and last-record events.

Applies to
----------

Prerequisites
-------------

.. only:: eventreporter

   This procedure applies to EventReporter.

.. only:: winsyslog or winsyslog_j

   This procedure applies to WinSyslog.

.. only:: mwagent

   This procedure applies to MonitorWare Agent.

.. only:: rsyslog

   This procedure applies to rsyslog Windows Agent.

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Run diagnostic checks before changing configuration.
- Remove passwords, private keys, license data, and other secrets from evidence.

Configuration paths
-------------------

.. only:: eventreporter

   **EventReporter:** Configuration Client > Services > File Monitor > affected service.

.. only:: winsyslog or winsyslog_j

   **WinSyslog:** Configuration Client > Services > File Monitor > affected service.

.. only:: mwagent

   **MonitorWare Agent:** Configuration Client > Services > File Monitor > affected service.

.. only:: rsyslog

   **rsyslog Windows Agent:** Configuration Client > Services > File Monitor > affected service.

Procedure
---------

#. Record source path, wildcard expansion, encoding, delimiter, and saved-position behavior.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-Item -LiteralPath '<SOURCE_FILE>' | Format-List FullName,Length,LastWriteTime,Attributes
      $s=[IO.File]::Open('<SOURCE_FILE>','Open','Read','ReadWrite'); $s.Length; $s.Close()
      Format-Hex -Path '<SOURCE_FILE>' -Count 32

   **Expected result:** The intended file is readable while the producer writes, and bytes match configured encoding/line endings.

   **If it fails:** Correct path, ACL/share mode, encoding, delimiter, or last-record delay before resetting position.

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

.. only:: winsyslog or winsyslog_j

   - WinSyslog Event ID 11074
   - WinSyslog Event ID 11075
   - WinSyslog Event ID 11076
   - WinSyslog Event ID 11077
   - WinSyslog Event ID 11078
   - WinSyslog Event ID 11079
   - WinSyslog Event ID 11080
   - WinSyslog Event ID 11081

.. only:: eventreporter

   - EventReporter Event ID 11074
   - EventReporter Event ID 11075
   - EventReporter Event ID 11076
   - EventReporter Event ID 11077
   - EventReporter Event ID 11078
   - EventReporter Event ID 11079
   - EventReporter Event ID 11080
   - EventReporter Event ID 11081

.. only:: mwagent

   - MonitorWare Agent Event ID 11074
   - MonitorWare Agent Event ID 11075
   - MonitorWare Agent Event ID 11076
   - MonitorWare Agent Event ID 11077
   - MonitorWare Agent Event ID 11078
   - MonitorWare Agent Event ID 11079
   - MonitorWare Agent Event ID 11080
   - MonitorWare Agent Event ID 11081

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11074
   - rsyslog Windows Agent Event ID 11075
   - rsyslog Windows Agent Event ID 11076
   - rsyslog Windows Agent Event ID 11077
   - rsyslog Windows Agent Event ID 11078
   - rsyslog Windows Agent Event ID 11079
   - rsyslog Windows Agent Event ID 11080
   - rsyslog Windows Agent Event ID 11081


Related procedures
------------------

- :doc:`Verify file paths, permissions, and free space <file-verify-path-permissions-and-disk-space>`
