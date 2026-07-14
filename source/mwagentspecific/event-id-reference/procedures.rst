.. _mwagent-event-id-procedures:

.. meta::
   :description: Exact diagnostic procedures referenced by MonitorWare Agent Event ID pages.

MonitorWare Agent Event ID troubleshooting procedures
=====================================================

Use these procedures from the applicable Event ID page. Each procedure includes commands,
expected results, failure branches, recovery verification, and evidence collection.

- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.
- :ref:`Interpret a Windows or Winsock error code <event-id-procedure-windows-interpret-error-code>` — Translate a numeric code without losing its operation or subsystem context.
- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Test an ODBC connection in the product context <event-id-procedure-database-test-odbc-connection>` — Verify ODBC provider, architecture, authentication, connectivity, and a minimal query.
- :ref:`Test an OLE DB connection in the product context <event-id-procedure-database-test-oledb-connection>` — Verify OLE DB provider, architecture, authentication, connectivity, and a minimal query.
- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Verify a monitored remote service <event-id-procedure-probe-verify-remote-service>` — Confirm resolution, transport, protocol, credentials, expected response, and timing.
- :ref:`Verify a program or Windows-service control action <event-id-procedure-action-verify-program-or-service-control>` — Check target, arguments, working directory, account rights, and positive result.
- :ref:`Verify a UDP path without assuming delivery <event-id-procedure-network-verify-udp-path>` — Confirm receiver binding, firewall policy, and positive receipt for a paced sample.
- :ref:`Verify an SNMP trap sender and receiver path <event-id-procedure-snmp-verify-trap-path>` — Confirm transport, endpoint, SNMP version, security/community, OIDs, and receipt.
- :ref:`Verify Event Log channel access and bookmark state <event-id-procedure-eventlog-verify-channel-access-and-bookmark>` — Confirm channel existence, enablement, account access, and collection position.
- :ref:`Verify File Monitor source state and encoding <event-id-procedure-filemonitor-verify-source-state-and-encoding>` — Check source path, sharing, encoding, line endings, and read position.
- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :ref:`Verify Microsoft Message Queuing availability and access <event-id-procedure-msmq-verify-queue-access>` — Confirm feature, service, queue path, transaction mode, and send rights.
- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :ref:`Verify sender, receiver, and queued-message recovery <event-id-procedure-transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Verify SMTP connectivity and mail delivery <event-id-procedure-mail-verify-smtp-delivery>` — Separate DNS, TCP, TLS, authentication, relay, recipient, and downstream delivery.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
