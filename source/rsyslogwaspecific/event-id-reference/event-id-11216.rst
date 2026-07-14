:orphan:

.. _rsyslog-event-id-11216:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11216: Control Windows Service action could not open the target service.
   :event-id: 11216
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Control Windows Service action
   :event-reference: true

rsyslog Windows Agent Event ID 11216: Control Windows Service action could not open the target service
======================================================================================================

Answer
------

The action opened Service Control Manager but could not obtain the required handle for the configured target service. No start, stop, pause, or continue request is issued.

Event details
-------------

- **Event ID:** ``11216``
- **Severity:** Error
- **Component:** Control Windows Service action
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Could not open service '{service_name}'; Windows error {error_code}.`

Possible causes
---------------

- The configured Windows service name does not exist.
- The product service account lacks control access to the target service.
- The service was removed or became unavailable between configuration and execution.

Immediate checks
----------------

#. Translate the Windows error and verify the exact service name with the Windows Service Control Manager.
#. Confirm the product service account's permission to control that service.
#. Correct the name or permission and run one controlled action.

Detailed procedures
-------------------

- :ref:`Verify a program or Windows-service control action <event-id-procedure-action-verify-program-or-service-control>` — Check target, arguments, working directory, account rights, and positive result.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the target service handle opens and the intended action proceeds without Event ID 11216.

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

- :ref:`Event ID 11020 <rsyslog-event-id-11020>`
- :ref:`Event ID 11217 <rsyslog-event-id-11217>`
- :ref:`Event ID 11218 <rsyslog-event-id-11218>`
