:orphan:

.. _winsyslog-event-id-11118:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11118: Ping Probe service stopped after an unknown exception.
   :event-id: 11118
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Ping Probe service
   :event-reference: true

WinSyslog Event ID 11118: Ping Probe service stopped after an unknown exception
===============================================================================

Answer
------

The Ping Probe service raised an exception outside its normal diagnostic handling and no longer runs its polling loop.

Event details
-------------

- **Event ID:** ``11118``
- **Severity:** Error
- **Component:** Ping Probe service
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`The Ping Probe service encountered an unknown exception and stopped.`

Possible causes
---------------

- A network or ICMP provider raised an unexpected exception.
- System resource pressure disrupted the probe.
- The probe encountered a product defect.

Immediate checks
----------------

#. Confirm that the service is no longer producing probe results.
#. Collect neighboring events, Windows Error Reporting data, and a bounded debug log from one controlled restart.
#. Escalate a reproducible failure with the collected evidence.

Detailed procedures
-------------------

- :ref:`Verify a monitored remote service <event-id-procedure-probe-verify-remote-service>` — Confirm resolution, transport, protocol, credentials, expected response, and timing.
- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the Ping Probe remains active and produces controlled probe results without Event ID 11118.

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

- :ref:`Event ID 11117 <winsyslog-event-id-11117>`
