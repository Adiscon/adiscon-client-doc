:orphan:

.. _event-id-procedure-snmp-verify-trap-path:

.. meta::
   :description: Confirm transport, endpoint, SNMP version, security/community, OIDs, and receipt.
   :procedure-id: snmp.verify-trap-path
   :procedure-reference: true

Verify an SNMP trap sender and receiver path
============================================

When to use this procedure
--------------------------

Use for SNMP action, SNMP Trap Receiver, and SNMP Monitor.

Applies to
----------

This procedure applies to rsyslog Windows Agent.

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

#. Record transport, port, version, community/security profile, source, destination, and OIDs.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      Get-NetUDPEndpoint -LocalPort <PORT> | Format-Table LocalAddress,LocalPort,OwningProcess

   **Expected result:** The intended process owns the endpoint and records a unique test with expected OID and value.

   **If it fails:** Correct binding/firewall, then version, security, OID, variable type, or receiver filter.

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

- Use Wireshark only as an optional bounded packet capture.

Related Event IDs
-----------------

- :ref:`rsyslog Windows Agent Event ID 11016 <rsyslog-event-id-11016>`
- :ref:`rsyslog Windows Agent Event ID 11038 <rsyslog-event-id-11038>`
- :ref:`rsyslog Windows Agent Event ID 11132 <rsyslog-event-id-11132>`
- :ref:`rsyslog Windows Agent Event ID 11133 <rsyslog-event-id-11133>`
- :ref:`rsyslog Windows Agent Event ID 11134 <rsyslog-event-id-11134>`
- :ref:`rsyslog Windows Agent Event ID 11135 <rsyslog-event-id-11135>`
- :ref:`rsyslog Windows Agent Event ID 11136 <rsyslog-event-id-11136>`
- :ref:`rsyslog Windows Agent Event ID 11137 <rsyslog-event-id-11137>`
- :ref:`rsyslog Windows Agent Event ID 11138 <rsyslog-event-id-11138>`
- :ref:`rsyslog Windows Agent Event ID 11139 <rsyslog-event-id-11139>`
- :ref:`rsyslog Windows Agent Event ID 11140 <rsyslog-event-id-11140>`


Related procedures
------------------

- :ref:`Verify a UDP path without assuming delivery <event-id-procedure-network-verify-udp-path>`
- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>`
