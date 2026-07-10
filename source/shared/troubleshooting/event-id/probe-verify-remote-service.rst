:orphan:

.. _event-id-procedure-probe-verify-remote-service:

.. meta::
   :description: Confirm resolution, transport, protocol, credentials, expected response, and timing.
   :procedure-id: probe.verify-remote-service
   :procedure-reference: true

Verify a monitored remote service
=================================

When to use this procedure
--------------------------

Use for FTP, HTTP, IMAP, NNTP, Ping, POP3, SMTP, and related probes.

Applies to
----------

Prerequisites
-------------

.. only:: eventreporter

   This procedure applies to EventReporter.

.. only:: winsyslog or winsyslog_j

   This procedure applies to WinSyslog.

.. only:: mwagent

   This procedure applies to MonitorWare Agent.

.. only:: rsyslog

   This procedure applies to rsyslog Windows Agent.

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Run diagnostic checks before changing configuration.
- Remove passwords, private keys, license data, and other secrets from evidence.

Configuration paths
-------------------

.. only:: eventreporter

   **EventReporter:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: winsyslog or winsyslog_j

   **WinSyslog:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: mwagent

   **MonitorWare Agent:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: rsyslog

   **rsyslog Windows Agent:** Configuration Client > the service, rule, or action named on the Event ID page.

Procedure
---------

#. Record target, address family, port, TLS/authentication mode, timeout, and expected response.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Resolve-DnsName -Name '<HOST>'
      Test-NetConnection -ComputerName '<HOST>' -Port <PORT> -InformationLevel Detailed

   **Expected result:** The endpoint is reachable and the smallest safe protocol request returns the expected response within timeout.

   **If it fails:** Correct DNS, route, listener, TLS, credentials, path, expected response, or measured timeout.

#. Perform one uniquely identifiable product test through the same service, rule, or action.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output; do not change unrelated settings.

Verify the result
-----------------

Repeat the affected operation, confirm its positive output, and verify that queues, collection positions, or remote delivery continue normally.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- The command output, relevant configuration export, and bounded debug log from the same interval.

Related Event IDs
-----------------

.. only:: winsyslog or winsyslog_j

   - WinSyslog Event ID 11082
   - WinSyslog Event ID 11083
   - WinSyslog Event ID 11086
   - WinSyslog Event ID 11087
   - WinSyslog Event ID 11088
   - WinSyslog Event ID 11089
   - WinSyslog Event ID 11095
   - WinSyslog Event ID 11096
   - WinSyslog Event ID 11117
   - WinSyslog Event ID 11118
   - WinSyslog Event ID 11119
   - WinSyslog Event ID 11120
   - WinSyslog Event ID 11130
   - WinSyslog Event ID 11131

.. only:: eventreporter

   - EventReporter Event ID 11082
   - EventReporter Event ID 11083
   - EventReporter Event ID 11086
   - EventReporter Event ID 11087
   - EventReporter Event ID 11088
   - EventReporter Event ID 11089
   - EventReporter Event ID 11095
   - EventReporter Event ID 11096
   - EventReporter Event ID 11117
   - EventReporter Event ID 11118
   - EventReporter Event ID 11119
   - EventReporter Event ID 11120
   - EventReporter Event ID 11130
   - EventReporter Event ID 11131

.. only:: mwagent

   - MonitorWare Agent Event ID 11082
   - MonitorWare Agent Event ID 11083
   - MonitorWare Agent Event ID 11086
   - MonitorWare Agent Event ID 11087
   - MonitorWare Agent Event ID 11088
   - MonitorWare Agent Event ID 11089
   - MonitorWare Agent Event ID 11095
   - MonitorWare Agent Event ID 11096
   - MonitorWare Agent Event ID 11117
   - MonitorWare Agent Event ID 11118
   - MonitorWare Agent Event ID 11119
   - MonitorWare Agent Event ID 11120
   - MonitorWare Agent Event ID 11130
   - MonitorWare Agent Event ID 11131

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11082
   - rsyslog Windows Agent Event ID 11083
   - rsyslog Windows Agent Event ID 11086
   - rsyslog Windows Agent Event ID 11087
   - rsyslog Windows Agent Event ID 11088
   - rsyslog Windows Agent Event ID 11089
   - rsyslog Windows Agent Event ID 11095
   - rsyslog Windows Agent Event ID 11096
   - rsyslog Windows Agent Event ID 11117
   - rsyslog Windows Agent Event ID 11118
   - rsyslog Windows Agent Event ID 11119
   - rsyslog Windows Agent Event ID 11120
   - rsyslog Windows Agent Event ID 11130
   - rsyslog Windows Agent Event ID 11131


Related procedures
------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>`
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>`
