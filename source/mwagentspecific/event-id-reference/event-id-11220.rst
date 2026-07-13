:orphan:

.. _mwagent-event-id-11220:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11220: Control Windows Service action: runtime operation failed.
   :event-id: 11220
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Control Windows Service action
   :event-reference: true

MonitorWare Agent Event ID 11220: Control Windows Service action: runtime operation failed
==========================================================================================

Answer
------

Control Windows Service action: runtime operation failed. The product recorded this while processing control windows service action; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11220``
- **Severity:** Error
- **Component:** Control Windows Service action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Control Windows Service action: runtime operation failed. Additional detail: {event_detail}`

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

- :ref:`Verify a program or Windows-service control action <event-id-procedure-action-verify-program-or-service-control>` — Check target, arguments, working directory, account rights, and positive result.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11220 does not recur and that control windows service action processing continues.

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

- :ref:`Event ID 11020 <mwagent-event-id-11020>`
- :ref:`Event ID 11216 <mwagent-event-id-11216>`
- :ref:`Event ID 11217 <mwagent-event-id-11217>`
