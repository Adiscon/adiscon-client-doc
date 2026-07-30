:orphan:

.. _winsyslog-event-id-108:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 108: The service was stopped.
   :event-id: 108
   :event-product: WinSyslog
   :event-severity: Information
   :event-component: Windows service lifecycle
   :event-reference: true

WinSyslog Event ID 108: The service was stopped
===============================================

Answer
------

The product service completed shutdown.

Event details
-------------

- **Event ID:** ``108``
- **Severity:** Information
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The service was stopped.`

Possible causes
---------------

- Windows, an administrator, an installer, or product shutdown logic requested an orderly stop.

Immediate checks
----------------

#. No repair is required when the stop was intended.
#. If the stop was unexpected, inspect preceding product and Service Control Manager events for the initiating condition.
#. Distinguish this orderly stop from a process termination or crash before changing configuration.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that an intended stop leaves the service Stopped, or that an authorized restart remains Running and processes one identifiable event.

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

- :ref:`Event ID 100 <winsyslog-event-id-100>`
- :ref:`Event ID 101 <winsyslog-event-id-101>`
- :ref:`Event ID 102 <winsyslog-event-id-102>`
