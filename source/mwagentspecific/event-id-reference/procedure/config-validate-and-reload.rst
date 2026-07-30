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

Configuration Client > the service, rule, or action named on the Event ID page.

Procedure
---------

#. Export the pre-change configuration, then open only the exact service, ruleset, filter, or action named in the event.

   **Expected result:** The event detail and Configuration Client identify the same object and a readable pre-change export exists.

   **If it fails:** Do not infer the object from its type alone; collect the complete event and configuration export first.

#. Verify the backup metadata, then check required references, product availability, paths, addresses, ports, and credentials for that object only.

   .. code-block:: powershell

      Get-Item -LiteralPath '<CONFIG_EXPORT>' | Format-List FullName,Length,LastWriteTime

   **Expected result:** Every required reference resolves to an existing object and every selected feature is available in this product and edition.

   **If it fails:** Restore the export if the edited configuration cannot load; do not copy unsupported objects from another product or edition.

#. Save the smallest correction, reload the configuration using the Configuration Client's normal apply path, and run one identifiable test through the edited object.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Restore the pre-change export if loading fails, then collect the first new product event and bounded debug output without changing unrelated objects.

Rollback
--------

#. Restore the configuration export created before the change.
#. Reload the restored configuration and verify the previous behavior.

Verify the result
-----------------

Confirm that the corrected object loads, the intended destination records one identifiable test, and neighboring rules and services continue normally.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- The command output, relevant configuration export, and bounded debug log from the same interval.

Related Event IDs
-----------------

- :ref:`MonitorWare Agent Event ID 11006 <mwagent-event-id-11006>`
- :ref:`MonitorWare Agent Event ID 11007 <mwagent-event-id-11007>`
- :ref:`MonitorWare Agent Event ID 11009 <mwagent-event-id-11009>`
- :ref:`MonitorWare Agent Event ID 11014 <mwagent-event-id-11014>`
- :ref:`MonitorWare Agent Event ID 11019 <mwagent-event-id-11019>`
- :ref:`MonitorWare Agent Event ID 11022 <mwagent-event-id-11022>`
- :ref:`MonitorWare Agent Event ID 11023 <mwagent-event-id-11023>`
- :ref:`MonitorWare Agent Event ID 11024 <mwagent-event-id-11024>`
- :ref:`MonitorWare Agent Event ID 11025 <mwagent-event-id-11025>`
- :ref:`MonitorWare Agent Event ID 11026 <mwagent-event-id-11026>`
- :ref:`MonitorWare Agent Event ID 11033 <mwagent-event-id-11033>`
- :ref:`MonitorWare Agent Event ID 11037 <mwagent-event-id-11037>`
- :ref:`MonitorWare Agent Event ID 11045 <mwagent-event-id-11045>`
- :ref:`MonitorWare Agent Event ID 11046 <mwagent-event-id-11046>`
- :ref:`MonitorWare Agent Event ID 11047 <mwagent-event-id-11047>`
- :ref:`MonitorWare Agent Event ID 11058 <mwagent-event-id-11058>`
- :ref:`MonitorWare Agent Event ID 11064 <mwagent-event-id-11064>`
- :ref:`MonitorWare Agent Event ID 11065 <mwagent-event-id-11065>`
- :ref:`MonitorWare Agent Event ID 11123 <mwagent-event-id-11123>`
- :ref:`MonitorWare Agent Event ID 11124 <mwagent-event-id-11124>`
- :ref:`MonitorWare Agent Event ID 11125 <mwagent-event-id-11125>`
- :ref:`MonitorWare Agent Event ID 11173 <mwagent-event-id-11173>`
- :ref:`MonitorWare Agent Event ID 11183 <mwagent-event-id-11183>`
- :ref:`MonitorWare Agent Event ID 11184 <mwagent-event-id-11184>`
- :ref:`MonitorWare Agent Event ID 11185 <mwagent-event-id-11185>`
- :ref:`MonitorWare Agent Event ID 11187 <mwagent-event-id-11187>`
- :ref:`MonitorWare Agent Event ID 11189 <mwagent-event-id-11189>`
- :ref:`MonitorWare Agent Event ID 11191 <mwagent-event-id-11191>`
- :ref:`MonitorWare Agent Event ID 11192 <mwagent-event-id-11192>`
- :ref:`MonitorWare Agent Event ID 11193 <mwagent-event-id-11193>`


Related procedures
------------------

- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
