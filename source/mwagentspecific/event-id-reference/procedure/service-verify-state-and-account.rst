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

This procedure applies to MonitorWare Agent.

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

Configuration Client > Service; then Windows Services > the product service.

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

- :ref:`MonitorWare Agent Event ID 100 <mwagent-event-id-100>`
- :ref:`MonitorWare Agent Event ID 101 <mwagent-event-id-101>`
- :ref:`MonitorWare Agent Event ID 102 <mwagent-event-id-102>`
- :ref:`MonitorWare Agent Event ID 103 <mwagent-event-id-103>`
- :ref:`MonitorWare Agent Event ID 104 <mwagent-event-id-104>`
- :ref:`MonitorWare Agent Event ID 105 <mwagent-event-id-105>`
- :ref:`MonitorWare Agent Event ID 106 <mwagent-event-id-106>`
- :ref:`MonitorWare Agent Event ID 108 <mwagent-event-id-108>`
- :ref:`MonitorWare Agent Event ID 11059 <mwagent-event-id-11059>`
- :ref:`MonitorWare Agent Event ID 11111 <mwagent-event-id-11111>`
- :ref:`MonitorWare Agent Event ID 11152 <mwagent-event-id-11152>`
- :ref:`MonitorWare Agent Event ID 11167 <mwagent-event-id-11167>`
- :ref:`MonitorWare Agent Event ID 11168 <mwagent-event-id-11168>`
- :ref:`MonitorWare Agent Event ID 11169 <mwagent-event-id-11169>`
- :ref:`MonitorWare Agent Event ID 11194 <mwagent-event-id-11194>`
- :ref:`MonitorWare Agent Event ID 11215 <mwagent-event-id-11215>`
