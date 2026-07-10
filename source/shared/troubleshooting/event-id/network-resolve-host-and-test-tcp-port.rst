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

.. only:: winsyslog or winsyslog_j

   - WinSyslog Event ID 11000
   - WinSyslog Event ID 11001
   - WinSyslog Event ID 11002
   - WinSyslog Event ID 11003
   - WinSyslog Event ID 11004
   - WinSyslog Event ID 11017
   - WinSyslog Event ID 11018
   - WinSyslog Event ID 11034
   - WinSyslog Event ID 11035
   - WinSyslog Event ID 11039
   - WinSyslog Event ID 11040
   - WinSyslog Event ID 11048
   - WinSyslog Event ID 11049
   - WinSyslog Event ID 11050
   - WinSyslog Event ID 11051
   - WinSyslog Event ID 11052
   - WinSyslog Event ID 11053
   - WinSyslog Event ID 11054
   - WinSyslog Event ID 11055
   - WinSyslog Event ID 11056
   - WinSyslog Event ID 11057
   - WinSyslog Event ID 11060
   - WinSyslog Event ID 11061
   - WinSyslog Event ID 11062
   - WinSyslog Event ID 11063

.. only:: eventreporter

   - EventReporter Event ID 11000
   - EventReporter Event ID 11001
   - EventReporter Event ID 11002
   - EventReporter Event ID 11003
   - EventReporter Event ID 11004
   - EventReporter Event ID 11017
   - EventReporter Event ID 11018
   - EventReporter Event ID 11034
   - EventReporter Event ID 11035
   - EventReporter Event ID 11039
   - EventReporter Event ID 11040
   - EventReporter Event ID 11048
   - EventReporter Event ID 11049
   - EventReporter Event ID 11050
   - EventReporter Event ID 11051
   - EventReporter Event ID 11052
   - EventReporter Event ID 11053
   - EventReporter Event ID 11054
   - EventReporter Event ID 11055
   - EventReporter Event ID 11056
   - EventReporter Event ID 11057
   - EventReporter Event ID 11060
   - EventReporter Event ID 11061
   - EventReporter Event ID 11062
   - EventReporter Event ID 11063

.. only:: mwagent

   - MonitorWare Agent Event ID 11000
   - MonitorWare Agent Event ID 11001
   - MonitorWare Agent Event ID 11002
   - MonitorWare Agent Event ID 11003
   - MonitorWare Agent Event ID 11004
   - MonitorWare Agent Event ID 11017
   - MonitorWare Agent Event ID 11018
   - MonitorWare Agent Event ID 11034
   - MonitorWare Agent Event ID 11035
   - MonitorWare Agent Event ID 11039
   - MonitorWare Agent Event ID 11040
   - MonitorWare Agent Event ID 11048
   - MonitorWare Agent Event ID 11049
   - MonitorWare Agent Event ID 11050
   - MonitorWare Agent Event ID 11051
   - MonitorWare Agent Event ID 11052
   - MonitorWare Agent Event ID 11053
   - MonitorWare Agent Event ID 11054
   - MonitorWare Agent Event ID 11055
   - MonitorWare Agent Event ID 11056
   - MonitorWare Agent Event ID 11057
   - MonitorWare Agent Event ID 11060
   - MonitorWare Agent Event ID 11061
   - MonitorWare Agent Event ID 11062
   - MonitorWare Agent Event ID 11063

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11000
   - rsyslog Windows Agent Event ID 11001
   - rsyslog Windows Agent Event ID 11002
   - rsyslog Windows Agent Event ID 11003
   - rsyslog Windows Agent Event ID 11004
   - rsyslog Windows Agent Event ID 11017
   - rsyslog Windows Agent Event ID 11018
   - rsyslog Windows Agent Event ID 11034
   - rsyslog Windows Agent Event ID 11035
   - rsyslog Windows Agent Event ID 11039
   - rsyslog Windows Agent Event ID 11040
   - rsyslog Windows Agent Event ID 11048
   - rsyslog Windows Agent Event ID 11049
   - rsyslog Windows Agent Event ID 11050
   - rsyslog Windows Agent Event ID 11051
   - rsyslog Windows Agent Event ID 11052
   - rsyslog Windows Agent Event ID 11053
   - rsyslog Windows Agent Event ID 11054
   - rsyslog Windows Agent Event ID 11055
   - rsyslog Windows Agent Event ID 11056
   - rsyslog Windows Agent Event ID 11057
   - rsyslog Windows Agent Event ID 11060
   - rsyslog Windows Agent Event ID 11061
   - rsyslog Windows Agent Event ID 11062
   - rsyslog Windows Agent Event ID 11063


Related procedures
------------------

- :doc:`Verify listener binding and Windows Firewall rules <network-verify-listener-binding-and-firewall>`
- :doc:`Verify TLS certificates, private keys, and permitted peers <tls-verify-certificate-chain-and-peer>`
