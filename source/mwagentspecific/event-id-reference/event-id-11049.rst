:orphan:

.. _mwagent-event-id-11049:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11049: TLS CA certificate file could not be loaded.
   :event-id: 11049
   :event-product: MonitorWare Agent
   :event-severity: Warning
   :event-component: TLS certificate loading
   :event-reference: true

MonitorWare Agent Event ID 11049: TLS CA certificate file could not be loaded
=============================================================================

Answer
------

The product could not load the configured CA PEM file into the TLS trust store. Connections using certificate authentication cannot verify peer certificates with that trust anchor until the file loads.

Event details
-------------

- **Event ID:** ``11049``
- **Severity:** Warning
- **Component:** TLS certificate loading
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`TLS CA certificate file could not be loaded. Additional detail: {event_detail}`

Possible causes
---------------

- The configured CA path is wrong, the file is missing, or the product service account cannot read it.
- The file is empty, damaged, uses an unsupported encoding, or does not contain a valid PEM CA certificate.

Immediate checks
----------------

#. Record the configured CA PEM path and the complete OpenSSL detail from the event.
#. Confirm that the service account can read the file and that certutil identifies it as the intended CA certificate, not a leaf certificate.
#. Correct the path or permissions, or replace the file with the intended PEM CA chain; reload the affected object and run one certificate-authenticated TLS test.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Reload or restart the affected TLS object, confirm that Event ID 11049 does not recur, and complete one certificate-authenticated TLS exchange that positively delivers a test message.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product version, affected listener or action, TLS mode, service account, and event timestamp with time zone.
- The redacted CA path, file metadata, certutil output, configuration export, and bounded debug log; do not include private keys.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11050 <mwagent-event-id-11050>`
- :ref:`Event ID 11051 <mwagent-event-id-11051>`
