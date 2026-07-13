:orphan:

.. _event-id-procedure-network-resolve-host-and-test-tcp-port:

.. meta::
   :description: Verify DNS, selected address, routing, and TCP establishment.
   :procedure-id: network.resolve-host-and-test-tcp-port
   :procedure-reference: true

Resolve a destination and test its TCP port
===========================================

When to use this procedure
--------------------------

Use for TCP syslog, SETP, RELP, SMTP, database, HTTP, and TCP probe connections.

Applies to
----------

This procedure applies to WinSyslog.

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

#. Record the configured destination host and port.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Resolve-DnsName -Name '<HOST>' | Format-Table Name,Type,IPAddress
      Test-NetConnection -ComputerName '<HOST>' -Port <PORT> -InformationLevel Detailed

   **Expected result:** The address is intended and TcpTestSucceeded is True.

   **If it fails:** Correct DNS, routing, firewall policy, NAT, port, or remote listener state.

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

- :ref:`WinSyslog Event ID 11000 <winsyslog-event-id-11000>`
- :ref:`WinSyslog Event ID 11001 <winsyslog-event-id-11001>`
- :ref:`WinSyslog Event ID 11002 <winsyslog-event-id-11002>`
- :ref:`WinSyslog Event ID 11003 <winsyslog-event-id-11003>`
- :ref:`WinSyslog Event ID 11004 <winsyslog-event-id-11004>`
- :ref:`WinSyslog Event ID 11017 <winsyslog-event-id-11017>`
- :ref:`WinSyslog Event ID 11018 <winsyslog-event-id-11018>`
- :ref:`WinSyslog Event ID 11034 <winsyslog-event-id-11034>`
- :ref:`WinSyslog Event ID 11035 <winsyslog-event-id-11035>`
- :ref:`WinSyslog Event ID 11039 <winsyslog-event-id-11039>`
- :ref:`WinSyslog Event ID 11040 <winsyslog-event-id-11040>`
- :ref:`WinSyslog Event ID 11048 <winsyslog-event-id-11048>`
- :ref:`WinSyslog Event ID 11049 <winsyslog-event-id-11049>`
- :ref:`WinSyslog Event ID 11050 <winsyslog-event-id-11050>`
- :ref:`WinSyslog Event ID 11051 <winsyslog-event-id-11051>`
- :ref:`WinSyslog Event ID 11052 <winsyslog-event-id-11052>`
- :ref:`WinSyslog Event ID 11053 <winsyslog-event-id-11053>`
- :ref:`WinSyslog Event ID 11054 <winsyslog-event-id-11054>`
- :ref:`WinSyslog Event ID 11055 <winsyslog-event-id-11055>`
- :ref:`WinSyslog Event ID 11056 <winsyslog-event-id-11056>`
- :ref:`WinSyslog Event ID 11057 <winsyslog-event-id-11057>`
- :ref:`WinSyslog Event ID 11060 <winsyslog-event-id-11060>`
- :ref:`WinSyslog Event ID 11061 <winsyslog-event-id-11061>`
- :ref:`WinSyslog Event ID 11062 <winsyslog-event-id-11062>`
- :ref:`WinSyslog Event ID 11063 <winsyslog-event-id-11063>`


Related procedures
------------------

- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>`
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>`
