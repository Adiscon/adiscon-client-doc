:orphan:

.. _event-id-procedure-mail-verify-smtp-delivery:

.. meta::
   :description: Separate DNS, TCP, TLS, authentication, relay, recipient, and downstream delivery.
   :procedure-id: mail.verify-smtp-delivery
   :procedure-reference: true

Verify SMTP connectivity and mail delivery
==========================================

When to use this procedure
--------------------------

Use for email actions, SMTP listeners, and SMTP probes.

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

#. Record server, port, TLS mode, authentication, sender, and recipient.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Resolve-DnsName -Name '<SMTP_HOST>'
      Test-NetConnection -ComputerName '<SMTP_HOST>' -Port <SMTP_PORT> -InformationLevel Detailed

   **Expected result:** TCP succeeds, the server accepts a unique product test, and the test mailbox receives it.

   **If it fails:** Use the first SMTP response code to correct TLS, authentication, relay, recipient, size, or content policy.

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

   - WinSyslog Event ID 11126
   - WinSyslog Event ID 11127
   - WinSyslog Event ID 11128
   - WinSyslog Event ID 11129
   - WinSyslog Event ID 11164
   - WinSyslog Event ID 11165

.. only:: eventreporter

   - EventReporter Event ID 11126
   - EventReporter Event ID 11127
   - EventReporter Event ID 11128
   - EventReporter Event ID 11129
   - EventReporter Event ID 11164
   - EventReporter Event ID 11165

.. only:: mwagent

   - MonitorWare Agent Event ID 11126
   - MonitorWare Agent Event ID 11127
   - MonitorWare Agent Event ID 11128
   - MonitorWare Agent Event ID 11129
   - MonitorWare Agent Event ID 11164
   - MonitorWare Agent Event ID 11165

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11126
   - rsyslog Windows Agent Event ID 11127
   - rsyslog Windows Agent Event ID 11128
   - rsyslog Windows Agent Event ID 11129
   - rsyslog Windows Agent Event ID 11164
   - rsyslog Windows Agent Event ID 11165


Related procedures
------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>`
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>`
