:orphan:

.. _winsyslog-event-id-11071:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11071: Disk Space Monitor service: runtime operation failed.
   :event-id: 11071
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Disk Space Monitor service
   :event-reference: true

WinSyslog Event ID 11071: Disk Space Monitor service: runtime operation failed
==============================================================================

Answer
------

Disk Space Monitor service: runtime operation failed. The product recorded this while processing disk space monitor service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11071``
- **Severity:** Error
- **Component:** Disk Space Monitor service
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Disk Space Monitor service: runtime operation failed. Additional detail: {event_detail}

Possible causes
---------------

- The product service, dependency, service account, or required Windows resource is unavailable or incorrectly configured.
- Windows returned the appended startup, shutdown, permission, timeout, or resource error.

Immediate checks
----------------

#. Record the affected service or component, service account, state, dependencies, and complete runtime detail.
#. Check recent Service Control Manager and neighboring product events for the first failure.
#. Correct the specific dependency, account, permission, or resource condition and perform one controlled retry.

Detailed procedures
-------------------

- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11071 does not recur and that disk space monitor service processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.
