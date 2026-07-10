:orphan:

.. _event-id-procedure-config-validate-and-reload:

.. meta::
   :description: Back up, inspect, correct, and test the exact invalid configuration object.
   :procedure-id: config.validate-and-reload
   :procedure-reference: true

Validate configuration and reload it safely
===========================================

When to use this procedure
--------------------------

Use for parsing, missing-object, unsupported-option, and reload events.

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

#. Export the configuration and open the exact service, rule, filter, or action named in the event.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-Item -LiteralPath '<CONFIG_EXPORT>' | Format-List FullName,Length,LastWriteTime

   **Expected result:** A readable pre-change backup exists and all required fields reference valid product objects.

   **If it fails:** Restore the export if the edited configuration cannot load; do not copy objects from another product manual.

#. Perform one uniquely identifiable product test through the same service, rule, or action.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output; do not change unrelated settings.

Rollback
--------

#. Restore the configuration export created before the change.
#. Reload the restored configuration and verify the previous behavior.

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

   - WinSyslog Event ID 11006
   - WinSyslog Event ID 11007
   - WinSyslog Event ID 11009
   - WinSyslog Event ID 11014
   - WinSyslog Event ID 11019
   - WinSyslog Event ID 11022
   - WinSyslog Event ID 11023
   - WinSyslog Event ID 11024
   - WinSyslog Event ID 11025
   - WinSyslog Event ID 11026
   - WinSyslog Event ID 11027
   - WinSyslog Event ID 11028
   - WinSyslog Event ID 11033
   - WinSyslog Event ID 11036
   - WinSyslog Event ID 11037
   - WinSyslog Event ID 11045
   - WinSyslog Event ID 11046
   - WinSyslog Event ID 11047
   - WinSyslog Event ID 11058
   - WinSyslog Event ID 11064
   - WinSyslog Event ID 11065
   - WinSyslog Event ID 11123
   - WinSyslog Event ID 11124
   - WinSyslog Event ID 11125
   - WinSyslog Event ID 11183
   - WinSyslog Event ID 11184
   - WinSyslog Event ID 11185
   - WinSyslog Event ID 11186
   - WinSyslog Event ID 11187
   - WinSyslog Event ID 11189
   - WinSyslog Event ID 11191
   - WinSyslog Event ID 11192
   - WinSyslog Event ID 11193

.. only:: eventreporter

   - EventReporter Event ID 11006
   - EventReporter Event ID 11007
   - EventReporter Event ID 11009
   - EventReporter Event ID 11014
   - EventReporter Event ID 11019
   - EventReporter Event ID 11022
   - EventReporter Event ID 11023
   - EventReporter Event ID 11024
   - EventReporter Event ID 11025
   - EventReporter Event ID 11026
   - EventReporter Event ID 11027
   - EventReporter Event ID 11028
   - EventReporter Event ID 11033
   - EventReporter Event ID 11036
   - EventReporter Event ID 11037
   - EventReporter Event ID 11045
   - EventReporter Event ID 11046
   - EventReporter Event ID 11047
   - EventReporter Event ID 11058
   - EventReporter Event ID 11064
   - EventReporter Event ID 11065
   - EventReporter Event ID 11123
   - EventReporter Event ID 11124
   - EventReporter Event ID 11125
   - EventReporter Event ID 11183
   - EventReporter Event ID 11184
   - EventReporter Event ID 11185
   - EventReporter Event ID 11186
   - EventReporter Event ID 11187
   - EventReporter Event ID 11189
   - EventReporter Event ID 11191
   - EventReporter Event ID 11192
   - EventReporter Event ID 11193

.. only:: mwagent

   - MonitorWare Agent Event ID 11006
   - MonitorWare Agent Event ID 11007
   - MonitorWare Agent Event ID 11009
   - MonitorWare Agent Event ID 11014
   - MonitorWare Agent Event ID 11019
   - MonitorWare Agent Event ID 11022
   - MonitorWare Agent Event ID 11023
   - MonitorWare Agent Event ID 11024
   - MonitorWare Agent Event ID 11025
   - MonitorWare Agent Event ID 11026
   - MonitorWare Agent Event ID 11027
   - MonitorWare Agent Event ID 11028
   - MonitorWare Agent Event ID 11033
   - MonitorWare Agent Event ID 11036
   - MonitorWare Agent Event ID 11037
   - MonitorWare Agent Event ID 11045
   - MonitorWare Agent Event ID 11046
   - MonitorWare Agent Event ID 11047
   - MonitorWare Agent Event ID 11058
   - MonitorWare Agent Event ID 11064
   - MonitorWare Agent Event ID 11065
   - MonitorWare Agent Event ID 11123
   - MonitorWare Agent Event ID 11124
   - MonitorWare Agent Event ID 11125
   - MonitorWare Agent Event ID 11183
   - MonitorWare Agent Event ID 11184
   - MonitorWare Agent Event ID 11185
   - MonitorWare Agent Event ID 11186
   - MonitorWare Agent Event ID 11187
   - MonitorWare Agent Event ID 11189
   - MonitorWare Agent Event ID 11191
   - MonitorWare Agent Event ID 11192
   - MonitorWare Agent Event ID 11193

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11006
   - rsyslog Windows Agent Event ID 11007
   - rsyslog Windows Agent Event ID 11009
   - rsyslog Windows Agent Event ID 11014
   - rsyslog Windows Agent Event ID 11019
   - rsyslog Windows Agent Event ID 11022
   - rsyslog Windows Agent Event ID 11023
   - rsyslog Windows Agent Event ID 11024
   - rsyslog Windows Agent Event ID 11025
   - rsyslog Windows Agent Event ID 11026
   - rsyslog Windows Agent Event ID 11027
   - rsyslog Windows Agent Event ID 11028
   - rsyslog Windows Agent Event ID 11033
   - rsyslog Windows Agent Event ID 11036
   - rsyslog Windows Agent Event ID 11037
   - rsyslog Windows Agent Event ID 11045
   - rsyslog Windows Agent Event ID 11046
   - rsyslog Windows Agent Event ID 11047
   - rsyslog Windows Agent Event ID 11058
   - rsyslog Windows Agent Event ID 11064
   - rsyslog Windows Agent Event ID 11065
   - rsyslog Windows Agent Event ID 11123
   - rsyslog Windows Agent Event ID 11124
   - rsyslog Windows Agent Event ID 11125
   - rsyslog Windows Agent Event ID 11183
   - rsyslog Windows Agent Event ID 11184
   - rsyslog Windows Agent Event ID 11185
   - rsyslog Windows Agent Event ID 11186
   - rsyslog Windows Agent Event ID 11187
   - rsyslog Windows Agent Event ID 11189
   - rsyslog Windows Agent Event ID 11191
   - rsyslog Windows Agent Event ID 11192
   - rsyslog Windows Agent Event ID 11193


Related procedures
------------------

- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
