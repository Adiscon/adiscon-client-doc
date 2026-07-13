:orphan:

.. _rsyslog-event-id-11162:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11162: Log rotation: runtime operation failed.
   :event-id: 11162
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

rsyslog Windows Agent Event ID 11162: Log rotation: runtime operation failed
============================================================================

Answer
------

Log rotation: runtime operation failed. The product recorded this while processing log rotation; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11162``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Logrotationsubsystem. Additional detail: {event_detail}`

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

- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11162 does not recur and that log rotation processing continues.

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

- :ref:`Event ID 11153 <rsyslog-event-id-11153>`
- :ref:`Event ID 11154 <rsyslog-event-id-11154>`
- :ref:`Event ID 11155 <rsyslog-event-id-11155>`
