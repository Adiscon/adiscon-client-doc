:orphan:

.. _winsyslog-event-id-11196:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11196: Disk queue: runtime data error.
   :event-id: 11196
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Disk queue
   :event-reference: true

WinSyslog Event ID 11196: Disk queue: runtime data error
========================================================

Answer
------

Disk queue: runtime data error. The product recorded this while processing disk queue; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11196``
- **Severity:** Error
- **Component:** Disk queue
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Formatted runtime diagnostic. Additional detail: {event_detail}`

Possible causes
---------------

- A downstream action is failing or retrying, so queued work cannot drain.
- The queue directory, permissions, free space, or queue artifact state prevents normal processing.

Immediate checks
----------------

#. Identify the first downstream action error and record queue depth and oldest-item time.
#. Check queue-directory access and free space without changing live queue files.
#. Correct the downstream cause, send one test event, and verify that the backlog decreases.

Detailed procedures
-------------------

- :ref:`Collect evidence for an escalation-only runtime event <event-id-procedure-runtime-collect-escalation-evidence>` — Capture a bounded reproducible support package without unsafe generic repair.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11196 does not recur and that disk queue processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

No safe general self-service repair is available for this event. Follow the escalation evidence procedure above and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11195 <winsyslog-event-id-11195>`
- :ref:`Event ID 11197 <winsyslog-event-id-11197>`
