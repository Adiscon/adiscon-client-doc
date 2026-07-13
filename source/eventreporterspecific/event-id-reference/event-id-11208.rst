:orphan:

.. _eventreporter-event-id-11208:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11208: Product service: configuration reload state.
   :event-id: 11208
   :event-product: EventReporter
   :event-severity: Information
   :event-component: Product service
   :event-reference: true

EventReporter Event ID 11208: Product service: configuration reload state
=========================================================================

Answer
------

Product service: configuration reload state. The product recorded this while processing product service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11208``
- **Severity:** Information
- **Component:** Product service
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Configuration reload successfully done. Additional detail: {event_detail}`

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

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11208 does not recur and that product service processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

This event normally records state rather than a failure. Escalate only when the state was unexpected or the associated operation does not recover.

Related Event IDs
-----------------

- :ref:`Event ID 11204 <eventreporter-event-id-11204>`
- :ref:`Event ID 11205 <eventreporter-event-id-11205>`
- :ref:`Event ID 11206 <eventreporter-event-id-11206>`
