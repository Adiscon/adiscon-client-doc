:orphan:

.. _winsyslog-event-id-11153:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11153: Log rotation: runtime operation failed.
   :event-id: 11153
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Log rotation
   :event-reference: true

WinSyslog Event ID 11153: Log rotation: runtime operation failed
================================================================

Answer
------

The log rotation reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11153``
- **Severity:** Warning
- **Component:** Log rotation
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Logrotationarchivemove.

Possible causes
---------------

- The configured path is unavailable, full, or inaccessible to the product service account.
- Another process is holding the file or the stored queue data is inconsistent.

Troubleshooting
---------------

#. Identify the affected path in the event detail.
#. Check free space, path existence, service-account permissions, and competing file locks.
#. Correct the storage condition and confirm that queue, file, or rotation processing resumes.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11153 does not recur and that log rotation processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the troubleshooting steps, collect the evidence above and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11154 <event-id-11154>`
- :doc:`Event ID 11155 <event-id-11155>`
- :doc:`Event ID 11156 <event-id-11156>`
