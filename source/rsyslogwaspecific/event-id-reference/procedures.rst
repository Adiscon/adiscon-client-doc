.. _rsyslog-event-id-procedures:

.. meta::
   :description: Exact diagnostic procedures referenced by rsyslog Windows Agent Event ID pages.

rsyslog Windows Agent Event ID troubleshooting procedures
=========================================================

Use these procedures from the applicable Event ID page. Each procedure includes commands,
expected results, failure branches, recovery verification, and evidence collection.

- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Collect evidence for an escalation-only runtime event <../../shared/troubleshooting/event-id/runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :doc:`Diagnose an action backlog or disk queue <../../shared/troubleshooting/event-id/queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :doc:`Diagnose log rotation and retention <../../shared/troubleshooting/event-id/file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.
- :doc:`Resolve a destination and test its TCP port <../../shared/troubleshooting/event-id/network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :doc:`Test an ODBC connection in the product context <../../shared/troubleshooting/event-id/database-test-odbc-connection>` — Verify ODBC provider, architecture, authentication, connectivity, and a minimal query.
- :doc:`Test an OLE DB connection in the product context <../../shared/troubleshooting/event-id/database-test-oledb-connection>` — Verify OLE DB provider, architecture, authentication, connectivity, and a minimal query.
- :doc:`Validate configuration and reload it safely <../../shared/troubleshooting/event-id/config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :doc:`Verify a monitored remote service <../../shared/troubleshooting/event-id/probe-verify-remote-service>` — Confirm resolution, transport, protocol, credentials, expected response, and timing.
- :doc:`Verify a program or Windows-service control action <../../shared/troubleshooting/event-id/action-verify-program-or-service-control>` — Check target, arguments, working directory, account rights, and positive result.
- :doc:`Verify a UDP path without assuming delivery <../../shared/troubleshooting/event-id/network-verify-udp-path>` — Confirm receiver binding, firewall policy, and positive receipt for a paced sample.
- :doc:`Verify an SNMP trap sender and receiver path <../../shared/troubleshooting/event-id/snmp-verify-trap-path>` — Confirm transport, endpoint, SNMP version, security/community, OIDs, and receipt.
- :doc:`Verify Event Log channel access and bookmark state <../../shared/troubleshooting/event-id/eventlog-verify-channel-access-and-bookmark>` — Confirm channel existence, enablement, account access, and collection position.
- :doc:`Verify File Monitor source state and encoding <../../shared/troubleshooting/event-id/filemonitor-verify-source-state-and-encoding>` — Check source path, sharing, encoding, line endings, and read position.
- :doc:`Verify file paths, permissions, and free space <../../shared/troubleshooting/event-id/file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :doc:`Verify listener binding and Windows Firewall rules <../../shared/troubleshooting/event-id/network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :doc:`Verify Microsoft Message Queuing availability and access <../../shared/troubleshooting/event-id/msmq-verify-queue-access>` — Confirm feature, service, queue path, transaction mode, and send rights.
- :doc:`Verify product license and feature entitlement state <../../shared/troubleshooting/event-id/license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :doc:`Verify sender, receiver, and queued-message recovery <../../shared/troubleshooting/event-id/transport-verify-sender-receiver-recovery>` — Prove end-to-end recovery and backlog drainage.
- :doc:`Verify service state, dependencies, and service account <../../shared/troubleshooting/event-id/service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :doc:`Verify SMTP connectivity and mail delivery <../../shared/troubleshooting/event-id/mail-verify-smtp-delivery>` — Separate DNS, TCP, TLS, authentication, relay, recipient, and downstream delivery.
- :doc:`Verify TLS certificates, private keys, and permitted peers <../../shared/troubleshooting/event-id/tls-verify-certificate-chain-and-peer>` — Check validity, trust chain, key pairing, protocol mode, and peer authorization.
