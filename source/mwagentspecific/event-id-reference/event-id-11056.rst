:orphan:

.. _mwagent-event-id-11056:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11056: TLS certificate-fingerprint authentication has no permitted peers.
   :event-id: 11056
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: TLS peer authorization
   :event-reference: true

MonitorWare Agent Event ID 11056: TLS certificate-fingerprint authentication has no permitted peers
===================================================================================================

Answer
------

The listener is configured for certificate-fingerprint authentication, but its permitted-peer list is empty. It therefore rejects every client certificate because no fingerprint can be authorized.

Event details
-------------

- **Event ID:** ``11056``
- **Severity:** Warning
- **Component:** TLS peer authorization
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`TLS certificate-fingerprint authentication has no permitted peers. Additional detail: {event_detail}`

Possible causes
---------------

- Certificate-fingerprint authentication was selected without adding any permitted certificate fingerprints.
- The permitted-peer entries were removed, saved under a different listener, or were not present in the configuration loaded by the service.

Immediate checks
----------------

#. Identify the affected listener and confirm that its TLS mode is certificate-fingerprint authentication.
#. Calculate the fingerprint from the authorized client's current certificate and compare its algorithm and format with the listener's permitted-peer requirements.
#. After verifying ownership, add the permitted fingerprint, save and reload the configuration, and retry one authorized client connection.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the intended client fingerprint completes TLS and delivers one test message, Event ID 11056 does not recur, and an unlisted fingerprint remains rejected.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product version, listener name, TLS mode, timestamp with time zone, and sanitized permitted-fingerprint configuration.
- The authorized client's sanitized certificate metadata and calculated fingerprint plus a bounded debug log; omit private keys and unrelated identities.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11053 <mwagent-event-id-11053>`
- :ref:`Event ID 11054 <mwagent-event-id-11054>`
- :ref:`Event ID 11055 <mwagent-event-id-11055>`
