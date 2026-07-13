:orphan:

.. _event-id-procedure-msmq-verify-queue-access:

.. meta::
   :description: Confirm feature, service, queue path, transaction mode, and send rights.
   :procedure-id: msmq.verify-queue-access
   :procedure-reference: true

Verify Microsoft Message Queuing availability and access
========================================================

When to use this procedure
--------------------------

Use for Microsoft Message Queuing action events.

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

Configuration Client > RuleSets > affected ruleset > rule > Send to Microsoft Message Queuing action.

Procedure
---------

#. Record exact private/public queue path, transactional mode, and product service account.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-WindowsOptionalFeature -Online -FeatureName MSMQ* | Format-Table FeatureName,State
      Get-Service -Name MSMQ | Format-List Status,StartType

   **Expected result:** Required MSMQ components run and a unique product test reaches the intended queue once.

   **If it fails:** Correct feature/service state, path, transaction mode, quota, network availability, or least-privilege send rights.

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

- :ref:`WinSyslog Event ID 11015 <winsyslog-event-id-11015>`
