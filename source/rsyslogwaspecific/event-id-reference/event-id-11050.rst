:orphan:

.. _rsyslog-event-id-11050:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11050: TLS certificate or private key could not be loaded.
   :event-id: 11050
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: TLS certificate loading
   :event-reference: true

rsyslog Windows Agent Event ID 11050: TLS certificate or private key could not be loaded
========================================================================================

Answer
------

The product could not load the configured local certificate and private key as a matching pair. The TLS endpoint can remain configured or listening, but handshakes that require its certificate cannot succeed until both files load.

Event details
-------------

- **Event ID:** ``11050``
- **Severity:** Warning
- **Component:** TLS certificate loading
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`TLS certificate or private key could not be loaded. Additional detail: {event_detail}`

Possible causes
---------------

- The private-key path points to a certificate request, certificate, or unrelated key instead of the matching private key.
- The private key is passphrase-encrypted, the certificate and key do not match, a file is malformed, or the service account cannot read one of the files.

Immediate checks
----------------

#. Preserve the configured certificate and key paths plus the complete OpenSSL detail; messages such as PEM lib, unable to get private key, and bad password read identify the failing file class.
#. Confirm that the key file contains an unencrypted private key rather than a certificate request, and verify that the certificate and key form a pair and are readable by the service account.
#. Back up the configuration, replace only the incorrect file or path, restrict the unencrypted key to the service account and administrators, then restart the affected service and send one test message.

Detailed procedures
-------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Restart the affected service, confirm that Event ID 11050 does not recur during certificate loading, and complete a TLS exchange that positively delivers one test message.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product version, affected listener or action, TLS mode, service account, and event timestamp with time zone.
- Redacted paths, file metadata, key-header classification, ACL output, configuration export, and bounded debug log; never provide the private key or its contents.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11049 <rsyslog-event-id-11049>`
- :ref:`Event ID 11051 <rsyslog-event-id-11051>`
- :ref:`Event ID 11052 <rsyslog-event-id-11052>`
