:orphan:

.. _eventreporter-event-id-11117:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11117: Ping Probe service stopped after a reported runtime error.
   :event-id: 11117
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Ping Probe service
   :event-reference: true

EventReporter Event ID 11117: Ping Probe service stopped after a reported runtime error
=======================================================================================

Answer
------

The Ping Probe service encountered a normal diagnostic exception outside an individual probe result and left its polling loop. The service will not produce further probe results until it is restarted or reloaded.

Event details
-------------

- **Event ID:** ``11117``
- **Severity:** Error
- **Component:** Ping Probe service
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Ping Probe error: {error_detail}`

Possible causes
---------------

- Probe initialization or a shared ICMP resource failed.
- The configured target or probe settings triggered a runtime error.
- Windows denied or could not provide a required network resource.

Immediate checks
----------------

#. Record the full error detail and identify the affected Ping Probe service.
#. Verify the target, service account, and local ICMP/network requirements.
#. Correct the reported cause and restart the affected service once.

Detailed procedures
-------------------

- :ref:`Verify a monitored remote service <event-id-procedure-probe-verify-remote-service>` — Confirm resolution, transport, protocol, credentials, expected response, and timing.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the Ping Probe produces new results for a controlled target without Event ID 11117.

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

- :ref:`Event ID 11118 <eventreporter-event-id-11118>`
