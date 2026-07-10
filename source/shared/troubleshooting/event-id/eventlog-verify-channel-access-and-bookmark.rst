:orphan:

.. _event-id-procedure-eventlog-verify-channel-access-and-bookmark:

.. meta::
   :description: Confirm channel existence, enablement, account access, and collection position.
   :procedure-id: eventlog.verify-channel-access-and-bookmark
   :procedure-reference: true

Verify Event Log channel access and bookmark state
==================================================

When to use this procedure
--------------------------

Use for Event Log Monitor and Event Log Monitor V2.

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

   **EventReporter:** Configuration Client > Services > Event Log Monitor or Event Log Monitor V2 > affected service.

.. only:: winsyslog or winsyslog_j

   **WinSyslog:** Configuration Client > Services > Event Log Monitor or Event Log Monitor V2 > affected service.

.. only:: mwagent

   **MonitorWare Agent:** Configuration Client > Services > Event Log Monitor or Event Log Monitor V2 > affected service.

.. only:: rsyslog

   **rsyslog Windows Agent:** Configuration Client > Services > Event Log Monitor or Event Log Monitor V2 > affected service.

Procedure
---------

#. Record exact channel name, collection mode, service account, and intended start position.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-WinEvent -ListLog '<CHANNEL_NAME>' | Format-List LogName,IsEnabled,RecordCount,LogMode
      Get-WinEvent -LogName '<CHANNEL_NAME>' -MaxEvents 5 | Format-List TimeCreated,Id,ProviderName,Message

   **Expected result:** The channel is enabled and readable in the service-account context; a test event is collected once.

   **If it fails:** Correct the channel name or least-privilege access; reset position only after recording replay impact.

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

   - WinSyslog Event ID 11097
   - WinSyslog Event ID 11098
   - WinSyslog Event ID 11099
   - WinSyslog Event ID 11100
   - WinSyslog Event ID 11101
   - WinSyslog Event ID 11102
   - WinSyslog Event ID 11103
   - WinSyslog Event ID 11104
   - WinSyslog Event ID 11105
   - WinSyslog Event ID 11106
   - WinSyslog Event ID 11107
   - WinSyslog Event ID 11108
   - WinSyslog Event ID 11109
   - WinSyslog Event ID 11110
   - WinSyslog Event ID 11147
   - WinSyslog Event ID 11148
   - WinSyslog Event ID 11149
   - WinSyslog Event ID 11150
   - WinSyslog Event ID 11151

.. only:: eventreporter

   - EventReporter Event ID 11097
   - EventReporter Event ID 11098
   - EventReporter Event ID 11099
   - EventReporter Event ID 11100
   - EventReporter Event ID 11101
   - EventReporter Event ID 11102
   - EventReporter Event ID 11103
   - EventReporter Event ID 11104
   - EventReporter Event ID 11105
   - EventReporter Event ID 11106
   - EventReporter Event ID 11107
   - EventReporter Event ID 11108
   - EventReporter Event ID 11109
   - EventReporter Event ID 11110
   - EventReporter Event ID 11147
   - EventReporter Event ID 11148
   - EventReporter Event ID 11149
   - EventReporter Event ID 11150
   - EventReporter Event ID 11151

.. only:: mwagent

   - MonitorWare Agent Event ID 11097
   - MonitorWare Agent Event ID 11098
   - MonitorWare Agent Event ID 11099
   - MonitorWare Agent Event ID 11100
   - MonitorWare Agent Event ID 11101
   - MonitorWare Agent Event ID 11102
   - MonitorWare Agent Event ID 11103
   - MonitorWare Agent Event ID 11104
   - MonitorWare Agent Event ID 11105
   - MonitorWare Agent Event ID 11106
   - MonitorWare Agent Event ID 11107
   - MonitorWare Agent Event ID 11108
   - MonitorWare Agent Event ID 11109
   - MonitorWare Agent Event ID 11110
   - MonitorWare Agent Event ID 11147
   - MonitorWare Agent Event ID 11148
   - MonitorWare Agent Event ID 11149
   - MonitorWare Agent Event ID 11150
   - MonitorWare Agent Event ID 11151

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11097
   - rsyslog Windows Agent Event ID 11098
   - rsyslog Windows Agent Event ID 11099
   - rsyslog Windows Agent Event ID 11100
   - rsyslog Windows Agent Event ID 11101
   - rsyslog Windows Agent Event ID 11102
   - rsyslog Windows Agent Event ID 11103
   - rsyslog Windows Agent Event ID 11104
   - rsyslog Windows Agent Event ID 11105
   - rsyslog Windows Agent Event ID 11106
   - rsyslog Windows Agent Event ID 11107
   - rsyslog Windows Agent Event ID 11108
   - rsyslog Windows Agent Event ID 11109
   - rsyslog Windows Agent Event ID 11110
   - rsyslog Windows Agent Event ID 11147
   - rsyslog Windows Agent Event ID 11148
   - rsyslog Windows Agent Event ID 11149
   - rsyslog Windows Agent Event ID 11150
   - rsyslog Windows Agent Event ID 11151
