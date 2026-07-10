:orphan:

.. _event-id-procedure-queue-diagnose-backlog-and-disk-queue:

.. meta::
   :description: Identify why queued work is not draining while preserving data.
   :procedure-id: queue.diagnose-backlog-and-disk-queue
   :procedure-reference: true

Diagnose an action backlog or disk queue
========================================

When to use this procedure
--------------------------

Use for action cache, queue manager, disk queue, retry, and saturation events.

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

- Do not delete, rename, copy over, or manually edit active queue files.
- Collect evidence before any support-directed recovery.

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

#. Record queue depth, oldest item time, target action, directory, and whether depth is increasing.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-ChildItem -LiteralPath '<QUEUE_DIRECTORY>' | Measure-Object -Property Length -Sum
      Get-PSDrive -Name '<DRIVE_LETTER>' | Format-List Used,Free

   **Expected result:** Queue files are readable, space remains, the downstream cause is corrected, and depth decreases.

   **If it fails:** Diagnose the first downstream error; never edit or delete live queue files.

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
   - WinSyslog Event ID 11170
   - WinSyslog Event ID 11171
   - WinSyslog Event ID 11172
   - WinSyslog Event ID 11173
   - WinSyslog Event ID 11174
   - WinSyslog Event ID 11176
   - WinSyslog Event ID 11178
   - WinSyslog Event ID 11179
   - WinSyslog Event ID 11180
   - WinSyslog Event ID 11181
   - WinSyslog Event ID 11182

.. only:: eventreporter

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
   - EventReporter Event ID 11170
   - EventReporter Event ID 11171
   - EventReporter Event ID 11172
   - EventReporter Event ID 11173
   - EventReporter Event ID 11174
   - EventReporter Event ID 11176
   - EventReporter Event ID 11178
   - EventReporter Event ID 11179
   - EventReporter Event ID 11180
   - EventReporter Event ID 11181
   - EventReporter Event ID 11182

.. only:: mwagent

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
   - MonitorWare Agent Event ID 11170
   - MonitorWare Agent Event ID 11171
   - MonitorWare Agent Event ID 11172
   - MonitorWare Agent Event ID 11173
   - MonitorWare Agent Event ID 11174
   - MonitorWare Agent Event ID 11176
   - MonitorWare Agent Event ID 11178
   - MonitorWare Agent Event ID 11179
   - MonitorWare Agent Event ID 11180
   - MonitorWare Agent Event ID 11181
   - MonitorWare Agent Event ID 11182

.. only:: rsyslog

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
   - rsyslog Windows Agent Event ID 11170
   - rsyslog Windows Agent Event ID 11171
   - rsyslog Windows Agent Event ID 11172
   - rsyslog Windows Agent Event ID 11173
   - rsyslog Windows Agent Event ID 11174
   - rsyslog Windows Agent Event ID 11176
   - rsyslog Windows Agent Event ID 11178
   - rsyslog Windows Agent Event ID 11179
   - rsyslog Windows Agent Event ID 11180
   - rsyslog Windows Agent Event ID 11181
   - rsyslog Windows Agent Event ID 11182


Related procedures
------------------

- :doc:`Verify sender, receiver, and queued-message recovery <transport-verify-sender-receiver-recovery>`
- :doc:`Verify file paths, permissions, and free space <file-verify-path-permissions-and-disk-space>`
