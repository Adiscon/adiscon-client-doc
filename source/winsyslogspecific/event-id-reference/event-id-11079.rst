:orphan:

.. _winsyslog-event-id-11079:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11079: File Monitor service: configured file could not be opened.
   :event-id: 11079
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: File Monitor service
   :event-reference: true

WinSyslog Event ID 11079: File Monitor service: configured file could not be opened
===================================================================================

Answer
------

The file monitor service reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11079``
- **Severity:** Error
- **Component:** File Monitor service
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Filemonitor filenotfound or pathnotfound.

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

Repeat or monitor the affected operation and confirm that Event ID 11079 does not recur and that file monitor service processing continues.

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

- :doc:`Event ID 11074 <event-id-11074>`
- :doc:`Event ID 11075 <event-id-11075>`
- :doc:`Event ID 11076 <event-id-11076>`
