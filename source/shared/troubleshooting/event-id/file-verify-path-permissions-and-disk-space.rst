:orphan:

.. _event-id-procedure-file-verify-path-permissions-and-disk-space:

.. meta::
   :description: Check expansion, existence, ACLs, service-account context, and storage.
   :procedure-id: file.verify-path-permissions-and-disk-space
   :procedure-reference: true

Verify file paths, permissions, and free space
==============================================

When to use this procedure
--------------------------

Use for file actions, File Monitor, queue files, debug logs, and rotation.

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

#. Resolve the exact local or UNC directory used by the service.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Test-Path -LiteralPath '<DIRECTORY_PATH>'
      Get-Acl -LiteralPath '<DIRECTORY_PATH>' | Format-List Owner,AccessToString
      Get-PSDrive -Name '<DRIVE_LETTER>' | Format-List Used,Free

   **Expected result:** The path exists, the service account has minimum required rights, and sufficient free space remains.

   **If it fails:** Correct expansion, share/NTFS permissions, availability, or storage without granting broad rights.

#. Perform one uniquely identifiable product test through the same service, rule, or action.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output; do not change unrelated settings.

Rollback
--------

#. Restore the previous path or ACL backup if the change prevents operation.

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

   - WinSyslog Event ID 11042
   - WinSyslog Event ID 11071
   - WinSyslog Event ID 11074
   - WinSyslog Event ID 11075
   - WinSyslog Event ID 11076
   - WinSyslog Event ID 11077
   - WinSyslog Event ID 11078
   - WinSyslog Event ID 11079
   - WinSyslog Event ID 11080
   - WinSyslog Event ID 11081

.. only:: eventreporter

   - EventReporter Event ID 11042
   - EventReporter Event ID 11071
   - EventReporter Event ID 11074
   - EventReporter Event ID 11075
   - EventReporter Event ID 11076
   - EventReporter Event ID 11077
   - EventReporter Event ID 11078
   - EventReporter Event ID 11079
   - EventReporter Event ID 11080
   - EventReporter Event ID 11081

.. only:: mwagent

   - MonitorWare Agent Event ID 11042
   - MonitorWare Agent Event ID 11071
   - MonitorWare Agent Event ID 11074
   - MonitorWare Agent Event ID 11075
   - MonitorWare Agent Event ID 11076
   - MonitorWare Agent Event ID 11077
   - MonitorWare Agent Event ID 11078
   - MonitorWare Agent Event ID 11079
   - MonitorWare Agent Event ID 11080
   - MonitorWare Agent Event ID 11081

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11042
   - rsyslog Windows Agent Event ID 11071
   - rsyslog Windows Agent Event ID 11074
   - rsyslog Windows Agent Event ID 11075
   - rsyslog Windows Agent Event ID 11076
   - rsyslog Windows Agent Event ID 11077
   - rsyslog Windows Agent Event ID 11078
   - rsyslog Windows Agent Event ID 11079
   - rsyslog Windows Agent Event ID 11080
   - rsyslog Windows Agent Event ID 11081
