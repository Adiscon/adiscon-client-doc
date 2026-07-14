:orphan:

.. _eventreporter-event-id-11169:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11169: Individual Ping Probe stopped after an unknown exception.
   :event-id: 11169
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Ping Probe
   :event-reference: true

EventReporter Event ID 11169: Individual Ping Probe stopped after an unknown exception
======================================================================================

Answer
------

The individual probe operation raised an exception outside its normal ICMP error handling. Its result is not reliable for that execution.

Event details
-------------

- **Event ID:** ``11169``
- **Severity:** Error
- **Component:** Ping Probe
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`The Ping Probe encountered an unknown exception and cannot return a valid result.`

Possible causes
---------------

- The ICMP or network provider raised an unexpected exception.
- System resource pressure disrupted the probe operation.
- The probe encountered a product defect.

Immediate checks
----------------

#. Record the target and neighboring product and Windows network events.
#. Run one controlled probe while collecting a bounded debug log and Windows Error Reporting data.
#. Escalate the reproducible exception with the collected evidence.

Detailed procedures
-------------------

- :ref:`Verify a monitored remote service <event-id-procedure-probe-verify-remote-service>` — Confirm resolution, transport, protocol, credentials, expected response, and timing.
- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that controlled probes return valid results without Event ID 11169.

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

- :ref:`Event ID 11152 <eventreporter-event-id-11152>`
- :ref:`Event ID 11194 <eventreporter-event-id-11194>`
- :ref:`Event ID 11203 <eventreporter-event-id-11203>`
