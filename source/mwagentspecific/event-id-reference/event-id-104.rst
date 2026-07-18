:orphan:

.. _mwagent-event-id-104:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 104: The service initialization process failed.
   :event-id: 104
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Windows service lifecycle
   :event-reference: true

MonitorWare Agent Event ID 104: The service initialization process failed
=========================================================================

Answer
------

Product initialization returned a failure to the Windows service wrapper, so the service does not enter the Running state. An earlier product event normally identifies the specific initialization failure.

Event details
-------------

- **Event ID:** ``104``
- **Severity:** Error
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The initialization process failed.`

Possible causes
---------------

- License validation, configuration loading, or input-service startup failed earlier in the same startup attempt.
- The service account cannot access a required file, registry key, network resource, provider, or certificate.
- A required Windows resource or product component failed during initialization.

Immediate checks
----------------

#. Find the first product error immediately before Event ID 104 in the same startup attempt; treat that earlier event as the primary cause.
#. Record the service account, registered executable path, dependencies, and complete Service Control Manager events for the attempt.
#. Correct only the specific earlier failure, then perform one controlled service start.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the service reaches Running, at least one configured input starts, and Event ID 104 does not recur during that start.

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

- :ref:`Event ID 100 <mwagent-event-id-100>`
- :ref:`Event ID 101 <mwagent-event-id-101>`
- :ref:`Event ID 102 <mwagent-event-id-102>`
