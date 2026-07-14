:orphan:

.. _eventreporter-event-id-11054:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11054: TLS certificate-name authentication has no permitted peers.
   :event-id: 11054
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: TLS peer authorization
   :event-reference: true

EventReporter Event ID 11054: TLS certificate-name authentication has no permitted peers
========================================================================================

Answer
------

The listener is configured for certificate-name authentication, but its permitted-peer list is empty. It therefore rejects every client certificate after chain verification because no certificate name can be authorized.

Event details
-------------

- **Event ID:** ``11054``
- **Severity:** Warning
- **Component:** TLS peer authorization
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`TLS certificate-name authentication has no permitted peers. Additional detail: {event_detail}`

Possible causes
---------------

- Certificate-name authentication was selected without adding any permitted certificate names.
- The permitted-peer entries were removed, saved under a different listener, or were not present in the configuration loaded by the service.

Immediate checks
----------------

#. Identify the affected listener and confirm that its TLS mode is certificate-name authentication.
#. Inspect that listener's permitted peers and derive the intended value from the authorized client's certificate CN or SAN, not from an unrelated system name.
#. After verifying ownership, add the permitted name, save and reload the configuration, and retry one authorized client connection.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the intended client name completes TLS and delivers one test message, Event ID 11054 does not recur, and an unlisted certificate name remains rejected.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product version, listener name, TLS mode, timestamp with time zone, and redacted permitted-peer configuration.
- The authorized client's sanitized certificate subject and SANs plus a bounded debug log; omit private keys and unrelated identities.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11052 <eventreporter-event-id-11052>`
- :ref:`Event ID 11053 <eventreporter-event-id-11053>`
- :ref:`Event ID 11056 <eventreporter-event-id-11056>`
