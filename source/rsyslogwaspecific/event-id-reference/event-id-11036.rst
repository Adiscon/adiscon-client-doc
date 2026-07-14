:orphan:

.. _rsyslog-event-id-11036:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11036: RELP delivery failed and the message was queued.
   :event-id: 11036
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: Send RELP action
   :event-reference: true

rsyslog Windows Agent Event ID 11036: RELP delivery failed and the message was queued
=====================================================================================

Answer
------

The Send RELP action could not transmit the current message, but action disk queuing was enabled and the product stored the message for later delivery.

Event details
-------------

- **Event ID:** ``11036``
- **Severity:** Warning
- **Component:** Send RELP action
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Error: {error_code} | Error sending RELP message: {error_detail}`

Possible causes
---------------

- The RELP peer is unavailable, refusing connections, or closing the session.
- DNS, routing, firewall, or TLS settings prevent communication.
- The peer rejected the RELP transaction or returned a protocol error.

Immediate checks
----------------

#. Record the RELP error and confirm that the action disk queue accepted the message.
#. Test name resolution, the configured TCP port, and any TLS peer requirements.
#. Restore the peer or network path and monitor queued replay.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the queued backlog drains and the RELP peer acknowledges a uniquely identifiable test message.

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

- :ref:`Event ID 11014 <rsyslog-event-id-11014>`
- :ref:`Event ID 11019 <rsyslog-event-id-11019>`
- :ref:`Event ID 11021 <rsyslog-event-id-11021>`
