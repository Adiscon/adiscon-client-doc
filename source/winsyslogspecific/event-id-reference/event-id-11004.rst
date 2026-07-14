:orphan:

.. _winsyslog-event-id-11004:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11004: SETP session restored.
   :event-id: 11004
   :event-product: WinSyslog
   :event-severity: Information
   :event-component: SETP sender
   :event-reference: true

WinSyslog Event ID 11004: SETP session restored
===============================================

Answer
------

Forwarding can continue.

Event details
-------------

- **Event ID:** ``11004``
- **Severity:** Information
- **Component:** SETP sender
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`SETP sender session has been restored. Additional detail: {event_detail}`

Possible causes
---------------

- The destination or listener is unavailable, blocked, bound to another address or port, or configured for a different transport.
- TLS certificates, peer authorization, protocol settings, or sender and receiver configuration do not match.

Immediate checks
----------------

#. Record the endpoint, address family, port, transport, TLS mode, and complete runtime detail.
#. Verify DNS, route, listener ownership, firewall policy, and TCP or UDP reachability as applicable.
#. Send one unique test message and verify positive receipt and queue recovery.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11004 does not recur and that setp sender processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

This event normally records state rather than a failure. Escalate only when the state was unexpected or the associated operation does not recover.

Related Event IDs
-----------------

- :ref:`Event ID 11000 <winsyslog-event-id-11000>`
- :ref:`Event ID 11001 <winsyslog-event-id-11001>`
- :ref:`Event ID 11002 <winsyslog-event-id-11002>`
