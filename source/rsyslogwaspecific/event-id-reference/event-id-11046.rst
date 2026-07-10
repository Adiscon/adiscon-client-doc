:orphan:

.. _rsyslog-event-id-11046:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11046: File-based configuration: file-based configuration could not be loaded.
   :event-id: 11046
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: File-based configuration
   :event-reference: true

rsyslog Windows Agent Event ID 11046: File-based configuration: file-based configuration could not be loaded
============================================================================================================

Answer
------

File-based configuration: file-based configuration could not be loaded. The product recorded this while processing file-based configuration; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11046``
- **Severity:** Error
- **Component:** File-based configuration
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Wszerr. Additional detail: {event_detail}

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

- :doc:`Validate configuration and reload it safely <../../shared/troubleshooting/event-id/config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11046 does not recur and that file-based configuration processing continues.

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

- :doc:`Event ID 11045 <event-id-11045>`
