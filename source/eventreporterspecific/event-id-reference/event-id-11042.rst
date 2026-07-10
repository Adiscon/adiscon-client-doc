:orphan:

.. _eventreporter-event-id-11042:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11042: WinSyslog file action: runtime operation failed.
   :event-id: 11042
   :event-product: EventReporter
   :event-severity: Error
   :event-component: WinSyslog file action
   :event-reference: true

EventReporter Event ID 11042: WinSyslog file action: runtime operation failed
=============================================================================

Answer
------

WinSyslog file action: runtime operation failed. The product recorded this while processing winsyslog file action; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11042``
- **Severity:** Error
- **Component:** WinSyslog file action
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** Writefile. Additional detail: {event_detail}

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

- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11042 does not recur and that winsyslog file action processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.
