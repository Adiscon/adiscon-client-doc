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

This procedure applies to rsyslog Windows Agent.

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

- :ref:`rsyslog Windows Agent Event ID 11006 <rsyslog-event-id-11006>`
- :ref:`rsyslog Windows Agent Event ID 11007 <rsyslog-event-id-11007>`
- :ref:`rsyslog Windows Agent Event ID 11009 <rsyslog-event-id-11009>`
- :ref:`rsyslog Windows Agent Event ID 11014 <rsyslog-event-id-11014>`
- :ref:`rsyslog Windows Agent Event ID 11019 <rsyslog-event-id-11019>`
- :ref:`rsyslog Windows Agent Event ID 11022 <rsyslog-event-id-11022>`
- :ref:`rsyslog Windows Agent Event ID 11023 <rsyslog-event-id-11023>`
- :ref:`rsyslog Windows Agent Event ID 11024 <rsyslog-event-id-11024>`
- :ref:`rsyslog Windows Agent Event ID 11025 <rsyslog-event-id-11025>`
- :ref:`rsyslog Windows Agent Event ID 11026 <rsyslog-event-id-11026>`
- :ref:`rsyslog Windows Agent Event ID 11027 <rsyslog-event-id-11027>`
- :ref:`rsyslog Windows Agent Event ID 11028 <rsyslog-event-id-11028>`
- :ref:`rsyslog Windows Agent Event ID 11033 <rsyslog-event-id-11033>`
- :ref:`rsyslog Windows Agent Event ID 11036 <rsyslog-event-id-11036>`
- :ref:`rsyslog Windows Agent Event ID 11037 <rsyslog-event-id-11037>`
- :ref:`rsyslog Windows Agent Event ID 11045 <rsyslog-event-id-11045>`
- :ref:`rsyslog Windows Agent Event ID 11046 <rsyslog-event-id-11046>`
- :ref:`rsyslog Windows Agent Event ID 11047 <rsyslog-event-id-11047>`
- :ref:`rsyslog Windows Agent Event ID 11058 <rsyslog-event-id-11058>`
- :ref:`rsyslog Windows Agent Event ID 11064 <rsyslog-event-id-11064>`
- :ref:`rsyslog Windows Agent Event ID 11065 <rsyslog-event-id-11065>`
- :ref:`rsyslog Windows Agent Event ID 11123 <rsyslog-event-id-11123>`
- :ref:`rsyslog Windows Agent Event ID 11124 <rsyslog-event-id-11124>`
- :ref:`rsyslog Windows Agent Event ID 11125 <rsyslog-event-id-11125>`
- :ref:`rsyslog Windows Agent Event ID 11183 <rsyslog-event-id-11183>`
- :ref:`rsyslog Windows Agent Event ID 11184 <rsyslog-event-id-11184>`
- :ref:`rsyslog Windows Agent Event ID 11185 <rsyslog-event-id-11185>`
- :ref:`rsyslog Windows Agent Event ID 11186 <rsyslog-event-id-11186>`
- :ref:`rsyslog Windows Agent Event ID 11187 <rsyslog-event-id-11187>`
- :ref:`rsyslog Windows Agent Event ID 11189 <rsyslog-event-id-11189>`
- :ref:`rsyslog Windows Agent Event ID 11191 <rsyslog-event-id-11191>`
- :ref:`rsyslog Windows Agent Event ID 11192 <rsyslog-event-id-11192>`
- :ref:`rsyslog Windows Agent Event ID 11193 <rsyslog-event-id-11193>`


Related procedures
------------------

- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
