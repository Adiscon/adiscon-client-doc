:orphan:

.. _winsyslog-event-id-11152:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11152: A queued event has an unsupported information-unit type.
   :event-id: 11152
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Event reconstruction
   :event-reference: true

WinSyslog Event ID 11152: A queued event has an unsupported information-unit type
=================================================================================

Answer
------

The product could not reconstruct an event from serialized queue data because its stored information-unit type is not recognized. That queued event is discarded.

Event details
-------------

- **Event ID:** ``11152``
- **Severity:** Error
- **Component:** Event reconstruction
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`A queued event contains invalid information-unit type {type_id}; the event was discarded.`

Possible causes
---------------

- Queue data was written by an incompatible product version.
- The serialized event or queue file is damaged.
- An unsupported component produced the information-unit type.

Immediate checks
----------------

#. Preserve the affected queue data and record the type identifier before changing files.
#. Confirm whether the queue was carried across a product downgrade, cross-product copy, or incompatible upgrade.
#. Collect configuration and debug evidence and contact support before deleting or replacing queue data.

Detailed procedures
-------------------

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that newly queued and replayed controlled events are reconstructed successfully without Event ID 11152.

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

- :ref:`Event ID 11169 <winsyslog-event-id-11169>`
- :ref:`Event ID 11194 <winsyslog-event-id-11194>`
