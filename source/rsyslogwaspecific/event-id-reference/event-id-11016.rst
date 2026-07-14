:orphan:

.. _rsyslog-event-id-11016:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11016: An SNMP trap variable contains an invalid OID.
   :event-id: 11016
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: Send SNMP Trap action
   :event-reference: true

rsyslog Windows Agent Event ID 11016: An SNMP trap variable contains an invalid OID
===================================================================================

Answer
------

The product could not parse or load the configured OID for one SNMP trap variable. That variable is removed from the action's active variable list.

Event details
-------------

- **Event ID:** ``11016``
- **Severity:** Warning
- **Component:** Send SNMP Trap action
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Please check your configuration, Error loading OID from var {variable_number}: {oid}, SNMP Error {snmp_error}`

Possible causes
---------------

- The OID is malformed or incomplete.
- The configured symbolic OID cannot be resolved by the available MIB data.
- The variable was imported from an incompatible or damaged configuration.

Immediate checks
----------------

#. Open the affected Send SNMP Trap action and locate the numbered variable from the event.
#. Replace the OID with a valid numeric OID or a resolvable symbolic OID.
#. Reload the configuration and send a controlled trap.

Detailed procedures
-------------------

- :ref:`Verify an SNMP trap sender and receiver path <event-id-procedure-snmp-verify-trap-path>` — Confirm transport, endpoint, SNMP version, security/community, OIDs, and receipt.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the controlled trap contains the expected variable and Event ID 11016 is not recorded during configuration loading.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11038 <rsyslog-event-id-11038>`
