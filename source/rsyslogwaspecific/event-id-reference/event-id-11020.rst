:orphan:

.. _rsyslog-event-id-11020:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11020: Control Windows Service action could not open Service Control Manager.
   :event-id: 11020
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Control Windows Service action
   :event-reference: true

rsyslog Windows Agent Event ID 11020: Control Windows Service action could not open Service Control Manager
===========================================================================================================

Answer
------

The action could not obtain the Windows Service Control Manager handle required to inspect or control the configured service.

Event details
-------------

- **Event ID:** ``11020``
- **Severity:** Error
- **Component:** Control Windows Service action
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Could not open Service Control Manager; Windows error {error_code}.`

Possible causes
---------------

- The product service account lacks Service Control Manager permissions.
- Windows denied the requested access because of local security policy.
- The Service Control Manager was temporarily unavailable.

Immediate checks
----------------

#. Translate the Windows error code from the event.
#. Confirm the product service account and its permission to manage the intended service.
#. Correct the account or policy and run a controlled service action.

Detailed procedures
-------------------

- :ref:`Verify a program or Windows-service control action <event-id-procedure-action-verify-program-or-service-control>` — Check target, arguments, working directory, account rights, and positive result.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the controlled action changes or queries the intended service and Event ID 11020 does not recur.

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

- :ref:`Event ID 11216 <rsyslog-event-id-11216>`
- :ref:`Event ID 11217 <rsyslog-event-id-11217>`
- :ref:`Event ID 11218 <rsyslog-event-id-11218>`
