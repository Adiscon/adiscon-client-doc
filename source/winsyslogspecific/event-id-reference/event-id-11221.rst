:orphan:

.. _winsyslog-event-id-11221:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11221: Target service did not reach the requested state before timeout.
   :event-id: 11221
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Control Windows Service action
   :event-reference: true

WinSyslog Event ID 11221: Target service did not reach the requested state before timeout
=========================================================================================

Answer
------

Windows accepted the service-control request, but the target service did not make the expected state progress within its wait interval. The action stops waiting.

Event details
-------------

- **Event ID:** ``11221``
- **Severity:** Error
- **Component:** Control Windows Service action
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Service action {action_id} for '{service_name}' did not complete within {timeout_ms} milliseconds.`

Possible causes
---------------

- The target service is hung or slow during start, stop, pause, or continue.
- A service dependency or shutdown task is blocked.
- The target service reported an unrealistic wait hint or stopped updating its checkpoint.

Immediate checks
----------------

#. Inspect the target service state, checkpoint, wait hint, and Windows events without immediately repeating the action.
#. Check dependencies, process responsiveness, and application-specific shutdown or startup work.
#. Recover the target service through its approved procedure, then run one controlled action.

Detailed procedures
-------------------

- :ref:`Verify a program or Windows-service control action <event-id-procedure-action-verify-program-or-service-control>` — Check target, arguments, working directory, account rights, and positive result.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the target service reaches the requested state within its wait interval and Event ID 11221 does not recur.

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

- :ref:`Event ID 11020 <winsyslog-event-id-11020>`
- :ref:`Event ID 11216 <winsyslog-event-id-11216>`
- :ref:`Event ID 11217 <winsyslog-event-id-11217>`
