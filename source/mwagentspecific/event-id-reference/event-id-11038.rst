:orphan:

.. _mwagent-event-id-11038:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11038: SNMP trap transmission failed.
   :event-id: 11038
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Send SNMP Trap action
   :event-reference: true

MonitorWare Agent Event ID 11038: SNMP trap transmission failed
===============================================================

Answer
------

The Send SNMP Trap action could not transmit a trap or replay a cached trap. If disk queuing is enabled, the product attempts to preserve the current message for retry.

Event details
-------------

- **Event ID:** ``11038``
- **Severity:** Error
- **Component:** Send SNMP Trap action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Error sending SNMP Trap. Error Code: '{error_code}'. Error Message: '{error_detail}'.`

Possible causes
---------------

- The trap destination is unreachable or not listening.
- The SNMP destination, version, credentials, or variable configuration is invalid.
- The action disk queue or replay operation failed.

Immediate checks
----------------

#. Record the error code and determine whether action disk queuing is enabled.
#. Verify the destination, UDP path, SNMP version, and configured trap variables.
#. Send a controlled trap and, when applicable, monitor the action queue.

Detailed procedures
-------------------

- :ref:`Verify an SNMP trap sender and receiver path <event-id-procedure-snmp-verify-trap-path>` — Confirm transport, endpoint, SNMP version, security/community, OIDs, and receipt.
- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the destination receives the controlled trap and any queued backlog decreases without another Event ID 11038.

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

- :ref:`Event ID 11016 <mwagent-event-id-11016>`
