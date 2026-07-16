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
- :ref:`WinSyslog Event ID 11187 <winsyslog-event-id-11187>`
- :ref:`WinSyslog Event ID 11189 <winsyslog-event-id-11189>`
- :ref:`WinSyslog Event ID 11191 <winsyslog-event-id-11191>`
- :ref:`WinSyslog Event ID 11192 <winsyslog-event-id-11192>`
- :ref:`WinSyslog Event ID 11193 <winsyslog-event-id-11193>`


Related procedures
------------------

- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>`
