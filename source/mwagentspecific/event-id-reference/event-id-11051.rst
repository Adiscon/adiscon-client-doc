:orphan:

.. _mwagent-event-id-11051:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11051: TLS client certificate verification failed.
   :event-id: 11051
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: TLS client certificate verification
   :event-reference: true

MonitorWare Agent Event ID 11051: TLS client certificate verification failed
============================================================================

Answer
------

During an incoming TLS handshake, OpenSSL returned a verification error for the client certificate. The listener rejects the connection unless the only error is certificate expiration and the listener is explicitly configured to allow expired certificates.

Event details
-------------

- **Event ID:** ``11051``
- **Severity:** Warning
- **Component:** TLS client certificate verification
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`TLS client certificate verification failed. Additional detail: {x509_verification_error}`

Possible causes
---------------

- The client certificate is expired or not yet valid, or its chain is missing an intermediate or does not lead to the configured CA.
- The certificate signature, purpose, issuer, or another X.509 validation requirement failed; the event detail contains the specific OpenSSL reason.

Immediate checks
----------------

#. Record the exact X.509 verification reason from the event and identify the client certificate presented during that handshake.
#. Verify the client certificate, its complete intermediate chain, the listener's CA PEM file, certificate purpose, and current system time.
#. Correct the client chain or listener trust configuration and retry one mutual-TLS session; do not make disabled validation the permanent repair.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Complete one mutual-TLS handshake from the affected client, positively verify receipt of its test message, and confirm that Event ID 11051 does not recur.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product version, listener name, TLS mode, event timestamp with time zone, and sanitized client-certificate subject, issuer, serial number, and validity dates.
- The listener CA and client-chain certutil output, configuration export, and bounded debug log; omit private keys and unrelated identities.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11049 <mwagent-event-id-11049>`
- :ref:`Event ID 11052 <mwagent-event-id-11052>`
- :ref:`Event ID 11053 <mwagent-event-id-11053>`
