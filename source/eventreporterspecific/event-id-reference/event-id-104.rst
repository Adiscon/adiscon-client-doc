:orphan:

.. _eventreporter-event-id-104:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 104: The service initialization process failed.
   :event-id: 104
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Windows service lifecycle
   :event-reference: true

EventReporter Event ID 104: The service initialization process failed
=====================================================================

Answer
------

The product service did not start.

Event details
-------------

- **Event ID:** ``104``
- **Severity:** Error
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The service initialization process failed. Additional detail: {event_detail}`

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

Repeat or monitor the affected operation and confirm that Event ID 104 does not recur and that windows service lifecycle processing continues.

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

- :ref:`Event ID 100 <eventreporter-event-id-100>`
- :ref:`Event ID 101 <eventreporter-event-id-101>`
- :ref:`Event ID 102 <eventreporter-event-id-102>`
