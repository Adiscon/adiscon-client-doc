:orphan:

.. _event-id-procedure-action-verify-program-or-service-control:

.. meta::
   :description: Check target, arguments, working directory, account rights, and positive result.
   :procedure-id: action.verify-program-or-service-control
   :procedure-reference: true

Verify a program or Windows-service control action
==================================================

When to use this procedure
--------------------------

Use for Start Program and Control Windows Service actions.

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

Configuration Client > RuleSets > affected ruleset > rule > affected action.

Procedure
---------

#. Record the full executable path or internal Windows service name, arguments, and service account.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Test-Path -LiteralPath '<EXECUTABLE_PATH>'
      Get-Acl -LiteralPath '<EXECUTABLE_PATH>' | Format-List AccessToString
      Get-Service -Name '<TARGET_SERVICE_NAME>' | Format-List Name,Status,StartType

   **Expected result:** The target exists and succeeds in the service-account context without an interactive desktop.

   **If it fails:** Correct full path, arguments, working directory, environment, ACLs, logon rights, or dependencies.

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

- :ref:`MonitorWare Agent Event ID 11020 <mwagent-event-id-11020>`
- :ref:`MonitorWare Agent Event ID 11041 <mwagent-event-id-11041>`
- :ref:`MonitorWare Agent Event ID 11216 <mwagent-event-id-11216>`
- :ref:`MonitorWare Agent Event ID 11217 <mwagent-event-id-11217>`
- :ref:`MonitorWare Agent Event ID 11218 <mwagent-event-id-11218>`
- :ref:`MonitorWare Agent Event ID 11219 <mwagent-event-id-11219>`
- :ref:`MonitorWare Agent Event ID 11220 <mwagent-event-id-11220>`
- :ref:`MonitorWare Agent Event ID 11221 <mwagent-event-id-11221>`


Related procedures
------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>`
