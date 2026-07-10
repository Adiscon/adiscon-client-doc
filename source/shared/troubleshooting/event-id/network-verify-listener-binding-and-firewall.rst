:orphan:

.. _event-id-procedure-network-verify-listener-binding-and-firewall:

.. meta::
   :description: Confirm effective address, port, transport, owning process, and inbound policy.
   :procedure-id: network.verify-listener-binding-and-firewall
   :procedure-reference: true

Verify listener binding and Windows Firewall rules
==================================================

When to use this procedure
--------------------------

Use when a listener cannot start or a remote sender cannot reach it.

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

#. Record the configured local address, address family, transport, and port.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-NetTCPConnection -State Listen -LocalPort <PORT> | Format-Table LocalAddress,LocalPort,OwningProcess
      Get-NetUDPEndpoint -LocalPort <PORT> | Format-Table LocalAddress,LocalPort,OwningProcess
      Get-NetFirewallRule -Enabled True -Direction Inbound | Get-NetFirewallPortFilter | Where-Object LocalPort -eq '<PORT>' | Format-Table Protocol,LocalPort

   **Expected result:** The intended process owns the endpoint and an approved allow rule covers its transport and profiles.

   **If it fails:** Correct wildcard/address conflicts or the narrow firewall rule; never disable Windows Firewall as a repair.

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

   - WinSyslog Event ID 11090
   - WinSyslog Event ID 11091
   - WinSyslog Event ID 11092
   - WinSyslog Event ID 11093
   - WinSyslog Event ID 11094
   - WinSyslog Event ID 11112
   - WinSyslog Event ID 11113
   - WinSyslog Event ID 11114
   - WinSyslog Event ID 11115
   - WinSyslog Event ID 11116
   - WinSyslog Event ID 11121
   - WinSyslog Event ID 11122
   - WinSyslog Event ID 11126
   - WinSyslog Event ID 11127
   - WinSyslog Event ID 11128
   - WinSyslog Event ID 11129
   - WinSyslog Event ID 11141
   - WinSyslog Event ID 11142
   - WinSyslog Event ID 11143
   - WinSyslog Event ID 11144
   - WinSyslog Event ID 11145
   - WinSyslog Event ID 11146
   - WinSyslog Event ID 11198
   - WinSyslog Event ID 11199
   - WinSyslog Event ID 11200
   - WinSyslog Event ID 11201
   - WinSyslog Event ID 11202

.. only:: eventreporter

   - EventReporter Event ID 11090
   - EventReporter Event ID 11091
   - EventReporter Event ID 11092
   - EventReporter Event ID 11093
   - EventReporter Event ID 11094
   - EventReporter Event ID 11112
   - EventReporter Event ID 11113
   - EventReporter Event ID 11114
   - EventReporter Event ID 11115
   - EventReporter Event ID 11116
   - EventReporter Event ID 11121
   - EventReporter Event ID 11122
   - EventReporter Event ID 11126
   - EventReporter Event ID 11127
   - EventReporter Event ID 11128
   - EventReporter Event ID 11129
   - EventReporter Event ID 11141
   - EventReporter Event ID 11142
   - EventReporter Event ID 11143
   - EventReporter Event ID 11144
   - EventReporter Event ID 11145
   - EventReporter Event ID 11146
   - EventReporter Event ID 11198
   - EventReporter Event ID 11199
   - EventReporter Event ID 11200
   - EventReporter Event ID 11201
   - EventReporter Event ID 11202

.. only:: mwagent

   - MonitorWare Agent Event ID 11090
   - MonitorWare Agent Event ID 11091
   - MonitorWare Agent Event ID 11092
   - MonitorWare Agent Event ID 11093
   - MonitorWare Agent Event ID 11094
   - MonitorWare Agent Event ID 11112
   - MonitorWare Agent Event ID 11113
   - MonitorWare Agent Event ID 11114
   - MonitorWare Agent Event ID 11115
   - MonitorWare Agent Event ID 11116
   - MonitorWare Agent Event ID 11121
   - MonitorWare Agent Event ID 11122
   - MonitorWare Agent Event ID 11126
   - MonitorWare Agent Event ID 11127
   - MonitorWare Agent Event ID 11128
   - MonitorWare Agent Event ID 11129
   - MonitorWare Agent Event ID 11141
   - MonitorWare Agent Event ID 11142
   - MonitorWare Agent Event ID 11143
   - MonitorWare Agent Event ID 11144
   - MonitorWare Agent Event ID 11145
   - MonitorWare Agent Event ID 11146
   - MonitorWare Agent Event ID 11198
   - MonitorWare Agent Event ID 11199
   - MonitorWare Agent Event ID 11200
   - MonitorWare Agent Event ID 11201
   - MonitorWare Agent Event ID 11202

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11090
   - rsyslog Windows Agent Event ID 11091
   - rsyslog Windows Agent Event ID 11092
   - rsyslog Windows Agent Event ID 11093
   - rsyslog Windows Agent Event ID 11094
   - rsyslog Windows Agent Event ID 11112
   - rsyslog Windows Agent Event ID 11113
   - rsyslog Windows Agent Event ID 11114
   - rsyslog Windows Agent Event ID 11115
   - rsyslog Windows Agent Event ID 11116
   - rsyslog Windows Agent Event ID 11121
   - rsyslog Windows Agent Event ID 11122
   - rsyslog Windows Agent Event ID 11126
   - rsyslog Windows Agent Event ID 11127
   - rsyslog Windows Agent Event ID 11128
   - rsyslog Windows Agent Event ID 11129
   - rsyslog Windows Agent Event ID 11141
   - rsyslog Windows Agent Event ID 11142
   - rsyslog Windows Agent Event ID 11143
   - rsyslog Windows Agent Event ID 11144
   - rsyslog Windows Agent Event ID 11145
   - rsyslog Windows Agent Event ID 11146
   - rsyslog Windows Agent Event ID 11198
   - rsyslog Windows Agent Event ID 11199
   - rsyslog Windows Agent Event ID 11200
   - rsyslog Windows Agent Event ID 11201
   - rsyslog Windows Agent Event ID 11202


Related procedures
------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>`
- :ref:`Verify a UDP path without assuming delivery <event-id-procedure-network-verify-udp-path>`
