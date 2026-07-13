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

This procedure applies to MonitorWare Agent.

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

- :ref:`MonitorWare Agent Event ID 11090 <mwagent-event-id-11090>`
- :ref:`MonitorWare Agent Event ID 11091 <mwagent-event-id-11091>`
- :ref:`MonitorWare Agent Event ID 11092 <mwagent-event-id-11092>`
- :ref:`MonitorWare Agent Event ID 11093 <mwagent-event-id-11093>`
- :ref:`MonitorWare Agent Event ID 11094 <mwagent-event-id-11094>`
- :ref:`MonitorWare Agent Event ID 11112 <mwagent-event-id-11112>`
- :ref:`MonitorWare Agent Event ID 11113 <mwagent-event-id-11113>`
- :ref:`MonitorWare Agent Event ID 11114 <mwagent-event-id-11114>`
- :ref:`MonitorWare Agent Event ID 11115 <mwagent-event-id-11115>`
- :ref:`MonitorWare Agent Event ID 11116 <mwagent-event-id-11116>`
- :ref:`MonitorWare Agent Event ID 11121 <mwagent-event-id-11121>`
- :ref:`MonitorWare Agent Event ID 11122 <mwagent-event-id-11122>`
- :ref:`MonitorWare Agent Event ID 11126 <mwagent-event-id-11126>`
- :ref:`MonitorWare Agent Event ID 11127 <mwagent-event-id-11127>`
- :ref:`MonitorWare Agent Event ID 11128 <mwagent-event-id-11128>`
- :ref:`MonitorWare Agent Event ID 11129 <mwagent-event-id-11129>`
- :ref:`MonitorWare Agent Event ID 11141 <mwagent-event-id-11141>`
- :ref:`MonitorWare Agent Event ID 11142 <mwagent-event-id-11142>`
- :ref:`MonitorWare Agent Event ID 11143 <mwagent-event-id-11143>`
- :ref:`MonitorWare Agent Event ID 11144 <mwagent-event-id-11144>`
- :ref:`MonitorWare Agent Event ID 11145 <mwagent-event-id-11145>`
- :ref:`MonitorWare Agent Event ID 11146 <mwagent-event-id-11146>`
- :ref:`MonitorWare Agent Event ID 11198 <mwagent-event-id-11198>`
- :ref:`MonitorWare Agent Event ID 11199 <mwagent-event-id-11199>`
- :ref:`MonitorWare Agent Event ID 11200 <mwagent-event-id-11200>`
- :ref:`MonitorWare Agent Event ID 11201 <mwagent-event-id-11201>`
- :ref:`MonitorWare Agent Event ID 11202 <mwagent-event-id-11202>`


Related procedures
------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>`
- :ref:`Verify a UDP path without assuming delivery <event-id-procedure-network-verify-udp-path>`
