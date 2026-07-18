:orphan:

.. _eventreporter-event-id-105:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 105: The service was started.
   :event-id: 105
   :event-product: EventReporter
   :event-severity: Information
   :event-component: Windows service lifecycle
   :event-reference: true

EventReporter Event ID 105: The service was started
===================================================

Answer
------

The product service entered its running state.

Event details
-------------

- **Event ID:** ``105``
- **Severity:** Information
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The service was started.`

Possible causes
---------------

- Windows started the product service and product initialization completed successfully.

Immediate checks
----------------

#. No repair is required when the start was intended.
#. If starts are unexpected or frequent, correlate this event with preceding stop, crash, restart-recovery, update, or administrative events.
#. Verify one configured input and destination instead of relying on service state alone.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the service remains Running and processes one identifiable event through the intended destination.

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

- :ref:`Event ID 100 <eventreporter-event-id-100>`
- :ref:`Event ID 101 <eventreporter-event-id-101>`
- :ref:`Event ID 102 <eventreporter-event-id-102>`
