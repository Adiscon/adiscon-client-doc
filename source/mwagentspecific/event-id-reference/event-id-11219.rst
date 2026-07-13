:orphan:

.. _mwagent-event-id-11219:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11219: Control Windows Service action could not pause the target service.
   :event-id: 11219
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Control Windows Service action
   :event-reference: true

MonitorWare Agent Event ID 11219: Control Windows Service action could not pause the target service
===================================================================================================

Answer
------

Windows rejected the action's pause request for the configured service. The target service does not enter the normal pause-pending path from this request.

Event details
-------------

- **Event ID:** ``11219``
- **Severity:** Error
- **Component:** Control Windows Service action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Could not send the pause control to service '{service_name}'; Windows error {error_code}.`

Possible causes
---------------

- The service does not accept pause controls or is already in an incompatible state.
- The product service account lacks control permission.
- The Service Control Manager or target service returned an operational error.

Immediate checks
----------------

#. Translate the Windows error and confirm that the service accepts pause and continue controls.
#. Test the pause with native Windows service tools under an authorized account.
#. Correct the service or permission problem and run one controlled action.

Detailed procedures
-------------------

- :ref:`Verify a program or Windows-service control action <event-id-procedure-action-verify-program-or-service-control>` — Check target, arguments, working directory, account rights, and positive result.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the target service reaches Paused and Event ID 11219 does not recur.

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

- :ref:`Event ID 11020 <mwagent-event-id-11020>`
- :ref:`Event ID 11216 <mwagent-event-id-11216>`
- :ref:`Event ID 11217 <mwagent-event-id-11217>`
