:orphan:

.. _eventreporter-event-id-11122:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11122: RELP listener stopped after an unknown exception.
   :event-id: 11122
   :event-product: EventReporter
   :event-severity: Error
   :event-component: RELP listener
   :event-reference: true

EventReporter Event ID 11122: RELP listener stopped after an unknown exception
==============================================================================

Answer
------

The RELP listener raised an exception outside its normal binding and protocol error handling. The product stops retrying the listener after the failure.

Event details
-------------

- **Event ID:** ``11122``
- **Severity:** Error
- **Component:** RELP listener
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`The RELP listener encountered an unknown exception and stopped retrying.`

Possible causes
---------------

- The RELP or TLS provider raised an unexpected exception.
- System resource pressure disrupted the listener.
- The listener encountered a product defect.

Immediate checks
----------------

#. Confirm whether the configured RELP port is still listening.
#. Collect neighboring events, Windows Error Reporting data, and a bounded debug log from one controlled restart.
#. Escalate a reproducible failure with the collected evidence.

Detailed procedures
-------------------

- :ref:`Verify listener binding and Windows Firewall rules <event-id-procedure-network-verify-listener-binding-and-firewall>` — Confirm effective address, port, transport, owning process, and inbound policy.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Identify CA, certificate, private-key, trust-chain, and permitted-peer failures without exposing private key material.
- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the RELP listener remains active and accepts a controlled session without Event ID 11122.

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

- :ref:`Event ID 11121 <eventreporter-event-id-11121>`
