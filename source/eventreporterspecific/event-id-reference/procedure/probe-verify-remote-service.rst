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

This procedure applies to EventReporter.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Run diagnostic checks before changing configuration.
- Remove passwords, private keys, license data, and other secrets from evidence.

Configuration path
------------------

Configuration Client > the service, rule, or action named on the Event ID page.

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

- :ref:`EventReporter Event ID 11082 <eventreporter-event-id-11082>`
- :ref:`EventReporter Event ID 11083 <eventreporter-event-id-11083>`
- :ref:`EventReporter Event ID 11086 <eventreporter-event-id-11086>`
- :ref:`EventReporter Event ID 11087 <eventreporter-event-id-11087>`
- :ref:`EventReporter Event ID 11088 <eventreporter-event-id-11088>`
- :ref:`EventReporter Event ID 11089 <eventreporter-event-id-11089>`
- :ref:`EventReporter Event ID 11095 <eventreporter-event-id-11095>`
- :ref:`EventReporter Event ID 11096 <eventreporter-event-id-11096>`
- :ref:`EventReporter Event ID 11117 <eventreporter-event-id-11117>`
- :ref:`EventReporter Event ID 11118 <eventreporter-event-id-11118>`
- :ref:`EventReporter Event ID 11119 <eventreporter-event-id-11119>`
- :ref:`EventReporter Event ID 11120 <eventreporter-event-id-11120>`
- :ref:`EventReporter Event ID 11130 <eventreporter-event-id-11130>`
- :ref:`EventReporter Event ID 11131 <eventreporter-event-id-11131>`


Related procedures
------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>`
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>`
