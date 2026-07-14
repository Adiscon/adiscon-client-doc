:orphan:

.. _mwagent-event-id-11052:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11052: TLS client certificate identity is unavailable.
   :event-id: 11052
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: TLS client certificate verification
   :event-reference: true

MonitorWare Agent Event ID 11052: TLS client certificate identity is unavailable
================================================================================

Answer
------

The certificate-authenticated listener could not obtain both a usable client certificate and its subject identity. This branch includes a client that sent no certificate, a certificate with no usable subject, or a subject-conversion failure, and the listener rejects the connection.

Event details
-------------

- **Event ID:** ``11052``
- **Severity:** Warning
- **Component:** TLS client certificate verification
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`TLS client certificate identity is unavailable. Additional detail: {event_detail}`

Possible causes
---------------

- The client is not configured to present a certificate, uses an authentication mode that does not send one, or selected the wrong certificate.
- The presented certificate has no usable subject identity or OpenSSL could not convert that subject for peer authorization.

Immediate checks
----------------

#. Confirm that the listener requires certificate authentication and identify the client involved in the rejected handshake.
#. Verify that the client presents the intended certificate and that certutil displays a usable subject and identity values.
#. Correct the client certificate selection or replace a malformed certificate, then retry one mutual-TLS session and verify message receipt.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Complete one mutual-TLS handshake with the intended client certificate, positively verify receipt of its test message, and confirm that Event ID 11052 does not recur.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product version, listener name, TLS mode, timestamp with time zone, and sanitized client-certificate metadata if a certificate was presented.
- The client and listener configuration exports plus a bounded handshake debug log; omit private keys and unrelated identities.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11051 <mwagent-event-id-11051>`
- :ref:`Event ID 11053 <mwagent-event-id-11053>`
- :ref:`Event ID 11054 <mwagent-event-id-11054>`
