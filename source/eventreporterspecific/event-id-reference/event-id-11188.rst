:orphan:

.. _eventreporter-event-id-11188:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11188: Service configuration: configured service feature is unavailable.
   :event-id: 11188
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Service configuration
   :event-reference: true

EventReporter Event ID 11188: Service configuration: configured service feature is unavailable
==============================================================================================

Answer
------

Service configuration: configured service feature is unavailable. The product recorded this while processing service configuration; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11188``
- **Severity:** Warning
- **Component:** Service configuration
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Service configuration: configured service feature is unavailable. Additional detail: {event_detail}

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

- :doc:`Collect evidence for an escalation-only runtime event <../../shared/troubleshooting/event-id/runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11188 does not recur and that service configuration processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

No safe general self-service repair is available for this event. Follow the escalation evidence procedure above and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11183 <event-id-11183>`
- :doc:`Event ID 11184 <event-id-11184>`
- :doc:`Event ID 11185 <event-id-11185>`
