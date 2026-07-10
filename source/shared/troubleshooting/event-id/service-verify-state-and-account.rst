:orphan:

.. _event-id-procedure-service-verify-state-and-account:

.. meta::
   :description: Confirm service state, start mode, dependencies, account, and SCM errors.
   :procedure-id: service.verify-state-and-account
   :procedure-reference: true

Verify service state, dependencies, and service account
=======================================================

When to use this procedure
--------------------------

Use for service startup, shutdown, permission, and monitoring events.

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

   **EventReporter:** Configuration Client > Service; then Windows Services > the product service.

.. only:: winsyslog or winsyslog_j

   **WinSyslog:** Configuration Client > Service; then Windows Services > the product service.

.. only:: mwagent

   **MonitorWare Agent:** Configuration Client > Service; then Windows Services > the product service.

.. only:: rsyslog

   **rsyslog Windows Agent:** Configuration Client > Service; then Windows Services > the product service.

Procedure
---------

#. Identify the internal Windows service name and intended service account.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-CimInstance Win32_Service -Filter "Name='<SERVICE_NAME>'" | Format-List Name,State,StartMode,StartName,ExitCode
      Get-Service -Name '<SERVICE_NAME>' -RequiredServices | Format-Table Name,Status,StartType

   **Expected result:** The service and required dependencies are in the intended state under the intended account.

   **If it fails:** Use recent Service Control Manager events to correct a dependency, logon, timeout, or termination failure.

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

   - WinSyslog Event ID 100
   - WinSyslog Event ID 101
   - WinSyslog Event ID 102
   - WinSyslog Event ID 103
   - WinSyslog Event ID 104
   - WinSyslog Event ID 105
   - WinSyslog Event ID 106
   - WinSyslog Event ID 108
   - WinSyslog Event ID 11059
   - WinSyslog Event ID 11111
   - WinSyslog Event ID 11152
   - WinSyslog Event ID 11167
   - WinSyslog Event ID 11168
   - WinSyslog Event ID 11169
   - WinSyslog Event ID 11194
   - WinSyslog Event ID 11210
   - WinSyslog Event ID 11215

.. only:: eventreporter

   - EventReporter Event ID 100
   - EventReporter Event ID 101
   - EventReporter Event ID 102
   - EventReporter Event ID 103
   - EventReporter Event ID 104
   - EventReporter Event ID 105
   - EventReporter Event ID 106
   - EventReporter Event ID 108
   - EventReporter Event ID 11059
   - EventReporter Event ID 11111
   - EventReporter Event ID 11152
   - EventReporter Event ID 11167
   - EventReporter Event ID 11168
   - EventReporter Event ID 11169
   - EventReporter Event ID 11194
   - EventReporter Event ID 11203
   - EventReporter Event ID 11204
   - EventReporter Event ID 11205
   - EventReporter Event ID 11206
   - EventReporter Event ID 11207
   - EventReporter Event ID 11208
   - EventReporter Event ID 11209
   - EventReporter Event ID 11215

.. only:: mwagent

   - MonitorWare Agent Event ID 100
   - MonitorWare Agent Event ID 101
   - MonitorWare Agent Event ID 102
   - MonitorWare Agent Event ID 103
   - MonitorWare Agent Event ID 104
   - MonitorWare Agent Event ID 105
   - MonitorWare Agent Event ID 106
   - MonitorWare Agent Event ID 108
   - MonitorWare Agent Event ID 11059
   - MonitorWare Agent Event ID 11111
   - MonitorWare Agent Event ID 11152
   - MonitorWare Agent Event ID 11167
   - MonitorWare Agent Event ID 11168
   - MonitorWare Agent Event ID 11169
   - MonitorWare Agent Event ID 11194
   - MonitorWare Agent Event ID 11215

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 100
   - rsyslog Windows Agent Event ID 101
   - rsyslog Windows Agent Event ID 102
   - rsyslog Windows Agent Event ID 103
   - rsyslog Windows Agent Event ID 104
   - rsyslog Windows Agent Event ID 105
   - rsyslog Windows Agent Event ID 106
   - rsyslog Windows Agent Event ID 108
   - rsyslog Windows Agent Event ID 11059
   - rsyslog Windows Agent Event ID 11111
   - rsyslog Windows Agent Event ID 11152
   - rsyslog Windows Agent Event ID 11167
   - rsyslog Windows Agent Event ID 11168
   - rsyslog Windows Agent Event ID 11169
   - rsyslog Windows Agent Event ID 11194
   - rsyslog Windows Agent Event ID 11211
   - rsyslog Windows Agent Event ID 11215
