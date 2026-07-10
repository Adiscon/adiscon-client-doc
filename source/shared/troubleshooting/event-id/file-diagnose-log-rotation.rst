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

   **EventReporter:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: winsyslog or winsyslog_j

   **WinSyslog:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: mwagent

   **MonitorWare Agent:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: rsyslog

   **rsyslog Windows Agent:** Configuration Client > the service, rule, or action named on the Event ID page.

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

.. only:: winsyslog or winsyslog_j

   - WinSyslog Event ID 11153
   - WinSyslog Event ID 11154
   - WinSyslog Event ID 11155
   - WinSyslog Event ID 11156
   - WinSyslog Event ID 11157
   - WinSyslog Event ID 11158
   - WinSyslog Event ID 11159
   - WinSyslog Event ID 11160
   - WinSyslog Event ID 11161
   - WinSyslog Event ID 11162
   - WinSyslog Event ID 11163
   - WinSyslog Event ID 11222

.. only:: eventreporter

   - EventReporter Event ID 11153
   - EventReporter Event ID 11154
   - EventReporter Event ID 11155
   - EventReporter Event ID 11156
   - EventReporter Event ID 11157
   - EventReporter Event ID 11158
   - EventReporter Event ID 11159
   - EventReporter Event ID 11160
   - EventReporter Event ID 11161
   - EventReporter Event ID 11162
   - EventReporter Event ID 11163
   - EventReporter Event ID 11222

.. only:: mwagent

   - MonitorWare Agent Event ID 11153
   - MonitorWare Agent Event ID 11154
   - MonitorWare Agent Event ID 11155
   - MonitorWare Agent Event ID 11156
   - MonitorWare Agent Event ID 11157
   - MonitorWare Agent Event ID 11158
   - MonitorWare Agent Event ID 11159
   - MonitorWare Agent Event ID 11160
   - MonitorWare Agent Event ID 11161
   - MonitorWare Agent Event ID 11162
   - MonitorWare Agent Event ID 11163
   - MonitorWare Agent Event ID 11222

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11153
   - rsyslog Windows Agent Event ID 11154
   - rsyslog Windows Agent Event ID 11155
   - rsyslog Windows Agent Event ID 11156
   - rsyslog Windows Agent Event ID 11157
   - rsyslog Windows Agent Event ID 11158
   - rsyslog Windows Agent Event ID 11159
   - rsyslog Windows Agent Event ID 11160
   - rsyslog Windows Agent Event ID 11161
   - rsyslog Windows Agent Event ID 11162
   - rsyslog Windows Agent Event ID 11163
   - rsyslog Windows Agent Event ID 11222


Related procedures
------------------

- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>`
