:orphan:

.. _eventreporter-event-id-11217:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11217: Control Windows Service action could not start the target service.
   :event-id: 11217
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Control Windows Service action
   :event-reference: true

EventReporter Event ID 11217: Control Windows Service action could not start the target service
===============================================================================================

Answer
------

Windows rejected the action's request to start the configured service. The target service does not enter the normal start-pending path from this request.

Event details
-------------

- **Event ID:** ``11217``
- **Severity:** Error
- **Component:** Control Windows Service action
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Could not start the target service; Windows error {error_code}.`

Possible causes
---------------

- A service dependency, logon account, executable, or startup configuration is invalid.
- The target service is disabled or already in an incompatible state.
- The product service account lacks permission to start it.

Immediate checks
----------------

#. Translate the Windows error and inspect the target service and its dependencies in Windows Event Viewer.
#. Test a start using native Windows service tools under an appropriately authorized account.
#. Correct the target-service failure and run one controlled action.

Detailed procedures
-------------------

- :ref:`Verify a program or Windows-service control action <event-id-procedure-action-verify-program-or-service-control>` — Check target, arguments, working directory, account rights, and positive result.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the target service reaches Running and Event ID 11217 does not recur.

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

- :ref:`Event ID 11020 <eventreporter-event-id-11020>`
- :ref:`Event ID 11216 <eventreporter-event-id-11216>`
- :ref:`Event ID 11218 <eventreporter-event-id-11218>`
