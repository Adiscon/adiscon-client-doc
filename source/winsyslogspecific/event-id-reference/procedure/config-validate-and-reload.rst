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

- :ref:`WinSyslog Event ID 11006 <winsyslog-event-id-11006>`
- :ref:`WinSyslog Event ID 11007 <winsyslog-event-id-11007>`
- :ref:`WinSyslog Event ID 11009 <winsyslog-event-id-11009>`
- :ref:`WinSyslog Event ID 11014 <winsyslog-event-id-11014>`
- :ref:`WinSyslog Event ID 11019 <winsyslog-event-id-11019>`
- :ref:`WinSyslog Event ID 11022 <winsyslog-event-id-11022>`
- :ref:`WinSyslog Event ID 11023 <winsyslog-event-id-11023>`
- :ref:`WinSyslog Event ID 11024 <winsyslog-event-id-11024>`
- :ref:`WinSyslog Event ID 11025 <winsyslog-event-id-11025>`
- :ref:`WinSyslog Event ID 11026 <winsyslog-event-id-11026>`
- :ref:`WinSyslog Event ID 11033 <winsyslog-event-id-11033>`
- :ref:`WinSyslog Event ID 11037 <winsyslog-event-id-11037>`
- :ref:`WinSyslog Event ID 11045 <winsyslog-event-id-11045>`
- :ref:`WinSyslog Event ID 11046 <winsyslog-event-id-11046>`
- :ref:`WinSyslog Event ID 11047 <winsyslog-event-id-11047>`
- :ref:`WinSyslog Event ID 11058 <winsyslog-event-id-11058>`
- :ref:`WinSyslog Event ID 11064 <winsyslog-event-id-11064>`
- :ref:`WinSyslog Event ID 11065 <winsyslog-event-id-11065>`
- :ref:`WinSyslog Event ID 11123 <winsyslog-event-id-11123>`
- :ref:`WinSyslog Event ID 11124 <winsyslog-event-id-11124>`
- :ref:`WinSyslog Event ID 11125 <winsyslog-event-id-11125>`
- :ref:`WinSyslog Event ID 11173 <winsyslog-event-id-11173>`
- :ref:`WinSyslog Event ID 11183 <winsyslog-event-id-11183>`
- :ref:`WinSyslog Event ID 11184 <winsyslog-event-id-11184>`
- :ref:`WinSyslog Event ID 11185 <winsyslog-event-id-11185>`
- :ref:`WinSyslog Event ID 11186 <winsyslog-event-id-11186>`
- :ref:`WinSyslog Event ID 11187 <winsyslog-event-id-11187>`
- :ref:`WinSyslog Event ID 11189 <winsyslog-event-id-11189>`
- :ref:`WinSyslog Event ID 11191 <winsyslog-event-id-11191>`
- :ref:`WinSyslog Event ID 11192 <winsyslog-event-id-11192>`
- :ref:`WinSyslog Event ID 11193 <winsyslog-event-id-11193>`


Related procedures
------------------

- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
