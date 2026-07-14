:orphan:

.. _eventreporter-event-id-11073:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11073: DTLS listener stopped after an unknown exception.
   :event-id: 11073
   :event-product: EventReporter
   :event-severity: Error
   :event-component: DTLS listener
   :event-reference: true

EventReporter Event ID 11073: DTLS listener stopped after an unknown exception
==============================================================================

Answer
------

The DTLS listener raised an exception outside its normal bind and transport error handling. The product stops the listener worker instead of continuing in an unknown state.

Event details
-------------

- **Event ID:** ``11073``
- **Severity:** Error
- **Component:** DTLS listener
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`The DTLS listener encountered an unknown exception and stopped its worker thread.`

Possible causes
---------------

- A TLS or network provider raised an unexpected exception.
- System resource pressure disrupted the listener.
- The listener encountered a product defect.

Immediate checks
----------------

#. Confirm that the listener is no longer receiving DTLS messages.
#. Collect neighboring events, Windows Error Reporting data, and a bounded debug log from one controlled restart.
#. Escalate the evidence instead of repeatedly restarting a reproducibly failing listener.

Detailed procedures
-------------------

- :ref:`Verify a UDP path without assuming delivery <event-id-procedure-network-verify-udp-path>` — Confirm receiver binding, firewall policy, and positive receipt for a paced sample.
- :ref:`Verify TLS certificates, private keys, and permitted peers <event-id-procedure-tls-verify-certificate-chain-and-peer>` — Check validity, trust chain, key pairing, protocol mode, and peer authorization.
- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm after corrective action that the DTLS listener remains running and receives a controlled message without Event ID 11073.

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

- :ref:`Event ID 11072 <eventreporter-event-id-11072>`
