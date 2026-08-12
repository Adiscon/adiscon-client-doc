:orphan:

.. _eventreporter-event-id-11227:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11227: Event rejected after shutdown intake closed.
   :event-id: 11227
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Main message queue
   :event-reference: true

EventReporter Event ID 11227: Event rejected after shutdown intake closed
=========================================================================

Answer
------

A producer submitted an event after all producer owners were expected to have stopped and queue intake had closed.

Event details
-------------

- **Event ID:** ``11227``
- **Severity:** Warning
- **Component:** Main message queue
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.08
- **Message pattern:** :spelling:ignore:`The main queue rejected an event because shutdown intake is closed. Additional detail: {event_detail}`

Possible causes
---------------

- A producer callback or child worker remained active beyond its documented join boundary.

Immediate checks
----------------

#. Identify the source active at shutdown and verify that its callbacks and child workers join before owner completion.

Detailed procedures
-------------------

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.

Verify the result
-----------------

Repeat the stop or reload and confirm that Event ID 11227 does not recur.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry.
- The source inventory, debug log, and queue drain snapshot.

Escalation
----------

No safe general self-service repair is available for this event. Follow the escalation evidence procedure above and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11223 <eventreporter-event-id-11223>`
- :ref:`Event ID 11224 <eventreporter-event-id-11224>`
