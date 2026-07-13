:orphan:

.. _eventreporter-event-id-11024:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11024: Configured action type is not recognized.
   :event-id: 11024
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Rule engine action
   :event-reference: true

EventReporter Event ID 11024: Configured action type is not recognized
======================================================================

Answer
------

The configuration contains an action type that this the product build cannot instantiate. The affected action cannot run.

Event details
-------------

- **Event ID:** ``11024``
- **Severity:** Error
- **Component:** Rule engine action
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Invalid action configured. The action type is not recognized.`

Possible causes
---------------

- The configuration came from a newer or incompatible product version.
- A manual configuration edit supplied an invalid action type.
- The configuration object is incomplete or damaged.

Immediate checks
----------------

#. Export and back up the current configuration.
#. Identify the affected action and compare its type with actions supported by the installed product version.
#. Recreate the action with a supported type or install the intended compatible version, then reload the configuration.

Detailed procedures
-------------------

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that configuration loading no longer records Event ID 11024 and a controlled event reaches the recreated action.

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
