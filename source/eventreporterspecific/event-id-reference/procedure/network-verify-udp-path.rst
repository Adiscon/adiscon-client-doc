:orphan:

.. _event-id-procedure-network-verify-udp-path:

.. meta::
   :description: Confirm receiver binding, firewall policy, and positive receipt for a paced sample.
   :procedure-id: network.verify-udp-path
   :procedure-reference: true

Verify a UDP path without assuming delivery
===========================================

When to use this procedure
--------------------------

Use for UDP syslog, SNMP traps, and DTLS.

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

#. Record sender, receiver, transport, local address, and destination port.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-NetUDPEndpoint -LocalPort <PORT> | Format-Table LocalAddress,LocalPort,OwningProcess
      Get-Process -Id <OWNING_PROCESS_ID> | Format-List Id,ProcessName,Path

   **Expected result:** The intended product process owns the expected endpoint and records a unique paced test.

   **If it fails:** Resolve bind/firewall issues and use bounded packet evidence before diagnosing parsing; UDP is best effort.

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

Optional tools
--------------

- Use Windows pktmon for a bounded capture.
- Wireshark is an optional alternative when native evidence is insufficient.

Related Event IDs
-----------------

- :ref:`EventReporter Event ID 11072 <eventreporter-event-id-11072>`
- :ref:`EventReporter Event ID 11073 <eventreporter-event-id-11073>`
- :ref:`EventReporter Event ID 11137 <eventreporter-event-id-11137>`
- :ref:`EventReporter Event ID 11138 <eventreporter-event-id-11138>`
- :ref:`EventReporter Event ID 11139 <eventreporter-event-id-11139>`
- :ref:`EventReporter Event ID 11140 <eventreporter-event-id-11140>`


Related procedures
------------------

- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>`
