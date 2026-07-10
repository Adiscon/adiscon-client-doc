:orphan:

.. _event-id-procedure-evidence-export-configuration-and-debug-log:

.. meta::
   :description: Create a text configuration export and time-bounded debug capture, then disable debugging.
   :procedure-id: evidence.export-configuration-and-debug-log
   :procedure-reference: true

Export configuration and collect a bounded debug log
====================================================

When to use this procedure
--------------------------

Use this when configuration or runtime sequencing must be reviewed.

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

- Disable debug logging immediately after the bounded capture.
- Remove credentials, private keys, license material, and unrelated customer data before sharing.

Configuration paths
-------------------

.. only:: eventreporter

   **EventReporter:** Configuration Client > Computer > Export Settings to Registry File; then General > Debug.

.. only:: winsyslog or winsyslog_j

   **WinSyslog:** Configuration Client > Computer > Export Settings to Registry File; then General > Debug.

.. only:: mwagent

   **MonitorWare Agent:** Configuration Client > Computer > Export Settings to Registry File; then General > Debug.

.. only:: rsyslog

   **rsyslog Windows Agent:** Configuration Client > Computer > Export Settings to Registry File; then General > Debug.

Procedure
---------

#. Export settings as a text registry file, then enable the minimum debug level that reproduces the problem.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-Item -LiteralPath '<CONFIG_EXPORT>' | Format-List FullName,Length,LastWriteTime
      Get-Item -LiteralPath '<DEBUG_LOG>' | Format-List FullName,Length,LastWriteTime

   **Expected result:** Both files exist, are readable, and cover the recorded reproduction interval.

   **If it fails:** Verify the service account can write the debug directory and restart only if the setting requires it.

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
   - WinSyslog Event ID 118
   - WinSyslog Event ID 125
   - WinSyslog Event ID 900
   - WinSyslog Event ID 901
   - WinSyslog Event ID 11000
   - WinSyslog Event ID 11001
   - WinSyslog Event ID 11002
   - WinSyslog Event ID 11003
   - WinSyslog Event ID 11004
   - WinSyslog Event ID 11005
   - WinSyslog Event ID 11006
   - WinSyslog Event ID 11007
   - WinSyslog Event ID 11009
   - WinSyslog Event ID 11010
   - WinSyslog Event ID 11011
   - WinSyslog Event ID 11012
   - WinSyslog Event ID 11013
   - WinSyslog Event ID 11014
   - WinSyslog Event ID 11015
   - WinSyslog Event ID 11016
   - WinSyslog Event ID 11017
   - WinSyslog Event ID 11018
   - WinSyslog Event ID 11019
   - WinSyslog Event ID 11020
   - WinSyslog Event ID 11022
   - WinSyslog Event ID 11023
   - WinSyslog Event ID 11024
   - WinSyslog Event ID 11025
   - WinSyslog Event ID 11026
   - WinSyslog Event ID 11027
   - WinSyslog Event ID 11028
   - WinSyslog Event ID 11029
   - This procedure is used by 174 additional Event IDs; use the product Event ID index to locate them.

.. only:: eventreporter

   - EventReporter Event ID 100
   - EventReporter Event ID 101
   - EventReporter Event ID 102
   - EventReporter Event ID 103
   - EventReporter Event ID 104
   - EventReporter Event ID 105
   - EventReporter Event ID 106
   - EventReporter Event ID 108
   - EventReporter Event ID 118
   - EventReporter Event ID 901
   - EventReporter Event ID 11000
   - EventReporter Event ID 11001
   - EventReporter Event ID 11002
   - EventReporter Event ID 11003
   - EventReporter Event ID 11004
   - EventReporter Event ID 11005
   - EventReporter Event ID 11006
   - EventReporter Event ID 11007
   - EventReporter Event ID 11009
   - EventReporter Event ID 11010
   - EventReporter Event ID 11011
   - EventReporter Event ID 11012
   - EventReporter Event ID 11013
   - EventReporter Event ID 11014
   - EventReporter Event ID 11015
   - EventReporter Event ID 11016
   - EventReporter Event ID 11017
   - EventReporter Event ID 11018
   - EventReporter Event ID 11019
   - EventReporter Event ID 11020
   - EventReporter Event ID 11022
   - EventReporter Event ID 11023
   - EventReporter Event ID 11024
   - EventReporter Event ID 11025
   - EventReporter Event ID 11026
   - EventReporter Event ID 11027
   - EventReporter Event ID 11028
   - EventReporter Event ID 11029
   - EventReporter Event ID 11030
   - EventReporter Event ID 11031
   - This procedure is used by 178 additional Event IDs; use the product Event ID index to locate them.

.. only:: mwagent

   - MonitorWare Agent Event ID 100
   - MonitorWare Agent Event ID 101
   - MonitorWare Agent Event ID 102
   - MonitorWare Agent Event ID 103
   - MonitorWare Agent Event ID 104
   - MonitorWare Agent Event ID 105
   - MonitorWare Agent Event ID 106
   - MonitorWare Agent Event ID 108
   - MonitorWare Agent Event ID 118
   - MonitorWare Agent Event ID 11000
   - MonitorWare Agent Event ID 11001
   - MonitorWare Agent Event ID 11002
   - MonitorWare Agent Event ID 11003
   - MonitorWare Agent Event ID 11004
   - MonitorWare Agent Event ID 11005
   - MonitorWare Agent Event ID 11006
   - MonitorWare Agent Event ID 11007
   - MonitorWare Agent Event ID 11009
   - MonitorWare Agent Event ID 11010
   - MonitorWare Agent Event ID 11011
   - MonitorWare Agent Event ID 11012
   - MonitorWare Agent Event ID 11013
   - MonitorWare Agent Event ID 11014
   - MonitorWare Agent Event ID 11015
   - MonitorWare Agent Event ID 11016
   - MonitorWare Agent Event ID 11017
   - MonitorWare Agent Event ID 11018
   - MonitorWare Agent Event ID 11019
   - MonitorWare Agent Event ID 11020
   - MonitorWare Agent Event ID 11022
   - MonitorWare Agent Event ID 11023
   - MonitorWare Agent Event ID 11024
   - MonitorWare Agent Event ID 11025
   - MonitorWare Agent Event ID 11026
   - MonitorWare Agent Event ID 11027
   - MonitorWare Agent Event ID 11028
   - MonitorWare Agent Event ID 11029
   - MonitorWare Agent Event ID 11030
   - MonitorWare Agent Event ID 11031
   - MonitorWare Agent Event ID 11032
   - This procedure is used by 170 additional Event IDs; use the product Event ID index to locate them.

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 100
   - rsyslog Windows Agent Event ID 101
   - rsyslog Windows Agent Event ID 102
   - rsyslog Windows Agent Event ID 103
   - rsyslog Windows Agent Event ID 104
   - rsyslog Windows Agent Event ID 105
   - rsyslog Windows Agent Event ID 106
   - rsyslog Windows Agent Event ID 108
   - rsyslog Windows Agent Event ID 118
   - rsyslog Windows Agent Event ID 11000
   - rsyslog Windows Agent Event ID 11001
   - rsyslog Windows Agent Event ID 11002
   - rsyslog Windows Agent Event ID 11003
   - rsyslog Windows Agent Event ID 11004
   - rsyslog Windows Agent Event ID 11005
   - rsyslog Windows Agent Event ID 11006
   - rsyslog Windows Agent Event ID 11007
   - rsyslog Windows Agent Event ID 11009
   - rsyslog Windows Agent Event ID 11010
   - rsyslog Windows Agent Event ID 11011
   - rsyslog Windows Agent Event ID 11012
   - rsyslog Windows Agent Event ID 11013
   - rsyslog Windows Agent Event ID 11014
   - rsyslog Windows Agent Event ID 11015
   - rsyslog Windows Agent Event ID 11016
   - rsyslog Windows Agent Event ID 11017
   - rsyslog Windows Agent Event ID 11018
   - rsyslog Windows Agent Event ID 11019
   - rsyslog Windows Agent Event ID 11020
   - rsyslog Windows Agent Event ID 11022
   - rsyslog Windows Agent Event ID 11023
   - rsyslog Windows Agent Event ID 11024
   - rsyslog Windows Agent Event ID 11025
   - rsyslog Windows Agent Event ID 11026
   - rsyslog Windows Agent Event ID 11027
   - rsyslog Windows Agent Event ID 11028
   - rsyslog Windows Agent Event ID 11029
   - rsyslog Windows Agent Event ID 11030
   - rsyslog Windows Agent Event ID 11031
   - rsyslog Windows Agent Event ID 11032
   - This procedure is used by 171 additional Event IDs; use the product Event ID index to locate them.
