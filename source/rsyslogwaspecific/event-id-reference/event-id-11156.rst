:orphan:

.. _rsyslog-event-id-11156:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11156: Log rotation: runtime operation failed.
   :event-id: 11156
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

rsyslog Windows Agent Event ID 11156: Log rotation: runtime operation failed
============================================================================

Answer
------

Log rotation: runtime operation failed. The product recorded this while processing log rotation; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11156``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Logrotationarchivemove. Additional detail: {event_detail}

Possible causes
---------------

- The configured path is unavailable, full, or not writable by the service account.
- Rotation naming, retention, timing, or another process holding the file prevents the required operation.

Immediate checks
----------------

#. Record the resolved path, file name, rotation trigger, and service-account context.
#. Check existence, ACLs, free space, current file sizes, and recent timestamps.
#. Perform one controlled write or rotation and verify that active output continues.

Detailed procedures
-------------------

- :doc:`Diagnose log rotation and retention <../../shared/troubleshooting/event-id/file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11156 does not recur and that log rotation processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11153 <event-id-11153>`
- :doc:`Event ID 11154 <event-id-11154>`
- :doc:`Event ID 11155 <event-id-11155>`
