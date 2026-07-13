:orphan:

.. _winsyslog-event-id-11146:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11146: Syslog listener stopped after an unknown exception.
   :event-id: 11146
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Syslog listener
   :event-reference: true

WinSyslog Event ID 11146: Syslog listener stopped after an unknown exception
============================================================================

Answer
------

The active Syslog listener raised an exception outside its normal binding and socket error handling. The product stops retrying that listener after the failure.

Event details
-------------

- **Event ID:** ``11146``
- **Severity:** Error
- **Component:** Syslog listener
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`The Syslog listener encountered an unknown exception and stopped retrying.`

Possible causes
---------------

- A socket or TLS provider raised an unexpected exception.
- System resource pressure disrupted the listener.
- The listener encountered a product defect.

Immediate checks
----------------

#. Confirm whether the configured syslog port and transport are still active.
#. Collect neighboring events, Windows Error Reporting data, and a bounded debug log from one controlled restart.
#. Escalate a reproducible failure with the collected evidence.

Detailed procedures
-------------------

- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the listener remains active and receives a controlled syslog message without Event ID 11146.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

No safe general self-service repair is available for this event. Follow the escalation evidence procedure above and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11112 <winsyslog-event-id-11112>`
- :ref:`Event ID 11113 <winsyslog-event-id-11113>`
- :ref:`Event ID 11114 <winsyslog-event-id-11114>`
