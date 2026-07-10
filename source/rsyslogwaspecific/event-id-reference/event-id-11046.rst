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

The file-based configuration reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11046``
- **Severity:** Error
- **Component:** File-based configuration
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Wszerr.

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

Repeat or monitor the affected operation and confirm that Event ID 11046 does not recur and that file-based configuration processing continues.

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

- :doc:`Event ID 11045 <event-id-11045>`
