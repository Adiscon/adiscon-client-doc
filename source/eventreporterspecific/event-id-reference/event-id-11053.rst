:orphan:

.. _eventreporter-event-id-11053:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11053: TLS client certificate does not match a permitted peer.
   :event-id: 11053
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: TLS peer authorization
   :event-reference: true

EventReporter Event ID 11053: TLS client certificate does not match a permitted peer
====================================================================================

Answer
------

The client certificate passed chain verification, but the listener could not authorize it against the configured permitted peers. In certificate-name mode, no permitted value matched the certificate CN or SAN; in fingerprint mode, no permitted SHA-1 or SHA-256 fingerprint matched.

Event details
-------------

- **Event ID:** ``11053``
- **Severity:** Warning
- **Component:** TLS peer authorization
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`TLS client certificate does not match a permitted peer. Additional detail: {rejected_peer_identity}`

Possible causes
---------------

- The permitted-peer list contains a different name, SAN, or fingerprint than the certificate presented by the client.
- The client certificate was renewed or replaced, or the listener uses the wrong peer-authorization mode or fingerprint format.

Immediate checks
----------------

#. Use the event detail to determine whether the rejected value was a certificate name or fingerprint and identify the affected listener.
#. Compare the presented certificate's CN and SAN values or calculated fingerprint with the listener's permitted peers and current authorization mode.
#. After independently verifying the client's identity and certificate ownership, correct the permitted value or client certificate and retry one TLS session.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the authorized client completes TLS and delivers one test message, that Event ID 11053 does not recur, and that a certificate outside the permitted-peer policy remains rejected.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product version, listener name, TLS authorization mode, timestamp with time zone, and sanitized permitted-peer values.
- The presented certificate's sanitized subject, SANs, issuer, serial number, and calculated fingerprint plus a bounded debug log; omit private keys.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11051 <eventreporter-event-id-11051>`
- :ref:`Event ID 11054 <eventreporter-event-id-11054>`
- :ref:`Event ID 11055 <eventreporter-event-id-11055>`
- :ref:`Event ID 11056 <eventreporter-event-id-11056>`
