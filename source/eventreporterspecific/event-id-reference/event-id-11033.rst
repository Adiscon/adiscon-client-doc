:orphan:

.. _eventreporter-event-id-11033:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11033: Post Process action ignored an unsupported parse type.
   :event-id: 11033
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Post Process action
   :event-reference: true

EventReporter Event ID 11033: Post Process action ignored an unsupported parse type
===================================================================================

Answer
------

The Post Process action encountered a parse instruction type that the installed product build does not support. That instruction is ignored and later processing may use incomplete properties.

Event details
-------------

- **Event ID:** ``11033``
- **Severity:** Error
- **Component:** Post Process action
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Unsupported parse type {parse_type} was detected. The syntax was ignored.`

Possible causes
---------------

- The configuration was created by an incompatible software version.
- A manual configuration edit introduced an invalid parse type.
- The Post Process configuration is damaged or incomplete.

Immediate checks
----------------

#. Export and back up the affected Post Process action.
#. Identify and remove or recreate the unsupported parse instruction using the installed Configuration Client.
#. Reload the configuration and test the affected input.

Detailed procedures
-------------------

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the expected properties are produced and Event ID 11033 is not recorded during the controlled test.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11014 <eventreporter-event-id-11014>`
- :ref:`Event ID 11019 <eventreporter-event-id-11019>`
- :ref:`Event ID 11021 <eventreporter-event-id-11021>`
