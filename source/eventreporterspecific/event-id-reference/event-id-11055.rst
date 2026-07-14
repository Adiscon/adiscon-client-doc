:orphan:

.. _eventreporter-event-id-11055:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11055: TLS client certificate fingerprint could not be computed.
   :event-id: 11055
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: TLS peer authorization
   :event-reference: true

EventReporter Event ID 11055: TLS client certificate fingerprint could not be computed
======================================================================================

Answer
------

The listener is configured for certificate-fingerprint authentication and could not compute the required SHA-1 digest from the verified client certificate. It rejects the connection before comparing the certificate with permitted fingerprints.

Event details
-------------

- **Event ID:** ``11055``
- **Severity:** Warning
- **Component:** TLS peer authorization
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`TLS client certificate fingerprint could not be computed. Additional detail: {event_detail}`

Possible causes
---------------

- The presented certificate has an unexpected or unsupported encoding that prevents fingerprint calculation.
- The cryptographic provider could not perform the digest operation, or a resource or library error occurred after certificate verification.

Immediate checks
----------------

#. Preserve the complete event and bounded debug log and identify the exact client certificate used for the rejected handshake.
#. Use certutil to dump and verify the certificate and reproduce the failure once with the same client and listener.
#. Replace the client certificate only if validation fails; if a valid certificate still triggers this event, collect the listed evidence and escalate without weakening peer authentication.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the listener computes and matches the authorized fingerprint, accepts one TLS test session, delivers its message, and no longer emits Event ID 11055.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product version, listener name, TLS mode, timestamp with time zone, OpenSSL detail, and sanitized permitted-fingerprint format.
- Certutil output and sanitized certificate subject, issuer, serial number, validity dates, and calculated fingerprints plus a bounded debug log; omit private keys.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11053 <eventreporter-event-id-11053>`
- :ref:`Event ID 11056 <eventreporter-event-id-11056>`
