:orphan:

.. _mwagent-event-id-11015:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11015: Microsoft Message Queuing action: Microsoft Message Queuing operation failed.
   :event-id: 11015
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Microsoft Message Queuing action
   :event-reference: true

MonitorWare Agent Event ID 11015: Microsoft Message Queuing action: Microsoft Message Queuing operation failed
==============================================================================================================

Answer
------

The microsoft message queuing action reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11015``
- **Severity:** Error
- **Component:** Microsoft Message Queuing action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Cactionconfigsendmsqueue initapis.

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

Repeat or monitor the affected operation and confirm that Event ID 11015 does not recur and that microsoft message queuing action processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the troubleshooting steps, collect the evidence above and contact Adiscon Support.
