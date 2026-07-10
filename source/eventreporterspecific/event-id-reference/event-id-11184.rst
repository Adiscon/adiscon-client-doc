:orphan:

.. _eventreporter-event-id-11184:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11184: Service configuration: memory reserve could not be allocated.
   :event-id: 11184
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Service configuration
   :event-reference: true

EventReporter Event ID 11184: Service configuration: memory reserve could not be allocated
==========================================================================================

Answer
------

Service configuration: memory reserve could not be allocated. The product recorded this while processing service configuration; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11184``
- **Severity:** Warning
- **Component:** Service configuration
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Service configuration: memory reserve could not be allocated. Additional detail: {event_detail}

Possible causes
---------------

- The product service, dependency, service account, or required Windows resource is unavailable or incorrectly configured.
- Windows returned the appended startup, shutdown, permission, timeout, or resource error.

Immediate checks
----------------

#. Record the affected service or component, service account, state, dependencies, and complete runtime detail.
#. Check recent Service Control Manager and neighboring product events for the first failure.
#. Correct the specific dependency, account, permission, or resource condition and perform one controlled retry.

Detailed procedures
-------------------

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11184 does not recur and that service configuration processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11183 <eventreporter-event-id-11183>`
- :ref:`Event ID 11185 <eventreporter-event-id-11185>`
- :ref:`Event ID 11186 <eventreporter-event-id-11186>`
