:orphan:

.. _winsyslog-event-id-11214:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11214: System exception in the queue worker thread.
   :event-id: 11214
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Queue manager
   :event-reference: true

WinSyslog Event ID 11214: System exception in the queue worker thread
=====================================================================

Answer
------

A protected system exception handler caught a Windows exception in this path.

Event details
-------------

- **Event ID:** ``11214``
- **Severity:** Error
- **Component:** Queue manager
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** System exception in the queue worker thread.

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

Repeat or monitor the affected operation and confirm that Event ID 11214 does not recur and that queue manager processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

No safe general self-service repair is available for this event. Collect the evidence above and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11170 <event-id-11170>`
- :doc:`Event ID 11171 <event-id-11171>`
- :doc:`Event ID 11172 <event-id-11172>`
