:orphan:

.. _mwagent-event-id-11190:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11190: Service configuration: configured feature is unavailable.
   :event-id: 11190
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: Service configuration
   :event-reference: true

MonitorWare Agent Event ID 11190: Service configuration: configured feature is unavailable
==========================================================================================

Answer
------

Service configuration: configured feature is unavailable. The product recorded this while processing service configuration; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11190``
- **Severity:** Warning
- **Component:** Service configuration
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Service configuration: configured feature is unavailable. Additional detail: {event_detail}

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

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11190 does not recur and that service configuration processing continues.

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

- :ref:`Event ID 11183 <mwagent-event-id-11183>`
- :ref:`Event ID 11184 <mwagent-event-id-11184>`
- :ref:`Event ID 11185 <mwagent-event-id-11185>`
