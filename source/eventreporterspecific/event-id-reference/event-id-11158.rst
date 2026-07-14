:orphan:

.. _eventreporter-event-id-11158:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11158: Empty log-rotation queue file could not be deleted.
   :event-id: 11158
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Log rotation queue
   :event-reference: true

EventReporter Event ID 11158: Empty log-rotation queue file could not be deleted
================================================================================

Answer
------

The durable log-rotation queue contains no jobs, but the product could not delete its now-empty queue file. No queued rotation job is reported lost by this event.

Event details
-------------

- **Event ID:** ``11158``
- **Severity:** Warning
- **Component:** Log rotation queue
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Could not delete empty log rotation queue file: {queue_path}`

Possible causes
---------------

- The queue file is locked by another process.
- The service account lacks delete permission in the data directory.
- Antivirus, backup, or storage software is holding the file.

Immediate checks
----------------

#. Confirm that the queue file is empty and preserve its metadata.
#. Check file locks and delete permission in the product data directory.
#. Remove the blocking condition and let the subsystem retry cleanup.

Detailed procedures
-------------------

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the empty queue file is removed or recreated normally and Event ID 11158 stops recurring.

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

- :ref:`Event ID 11153 <eventreporter-event-id-11153>`
- :ref:`Event ID 11154 <eventreporter-event-id-11154>`
- :ref:`Event ID 11155 <eventreporter-event-id-11155>`
