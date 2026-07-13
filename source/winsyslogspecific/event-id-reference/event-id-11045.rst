:orphan:

.. _winsyslog-event-id-11045:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11045: File-based configuration: file-based configuration could not be loaded.
   :event-id: 11045
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: File-based configuration
   :event-reference: true

WinSyslog Event ID 11045: File-based configuration: file-based configuration could not be loaded
================================================================================================

Answer
------

File-based configuration: file-based configuration could not be loaded. The product recorded this while processing file-based configuration; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11045``
- **Severity:** Error
- **Component:** File-based configuration
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Wszerr. Additional detail: {event_detail}`

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

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11045 does not recur and that file-based configuration processing continues.

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

- :ref:`Event ID 11046 <winsyslog-event-id-11046>`
