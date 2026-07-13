:orphan:

.. _eventreporter-event-id-11189:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11189: Input service could not find its assigned ruleset.
   :event-id: 11189
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Service configuration
   :event-reference: true

EventReporter Event ID 11189: Input service could not find its assigned ruleset
===============================================================================

Answer
------

A configured input service references a ruleset that does not exist. Because that service requires a ruleset, the product does not start it.

Event details
-------------

- **Event ID:** ``11189``
- **Severity:** Error
- **Component:** Service configuration
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`No ruleset was found for service '{service_name}'; requested ruleset was '{ruleset_name}'. The service was not started.`

Possible causes
---------------

- The assigned ruleset was renamed or deleted.
- The service contains an empty, misspelled, or stale ruleset name.
- A configuration import omitted the referenced ruleset.

Immediate checks
----------------

#. Open the affected service and record its assigned ruleset.
#. Confirm that a ruleset with that exact name exists.
#. Correct the assignment or restore the ruleset, then validate and reload the configuration.

Detailed procedures
-------------------

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the input service starts and a controlled event reaches the assigned ruleset without Event ID 11189.

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

- :ref:`Event ID 11183 <eventreporter-event-id-11183>`
- :ref:`Event ID 11184 <eventreporter-event-id-11184>`
- :ref:`Event ID 11185 <eventreporter-event-id-11185>`
