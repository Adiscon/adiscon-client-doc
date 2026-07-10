:orphan:

.. _mwagent-event-id-11177:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11177: Queue manager: queue capacity condition.
   :event-id: 11177
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Queue manager
   :event-reference: true

MonitorWare Agent Event ID 11177: Queue manager: queue capacity condition
=========================================================================

Answer
------

The queue manager reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11177``
- **Severity:** Error
- **Component:** Queue manager
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Runtime diagnostic.

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

Repeat or monitor the affected operation and confirm that Event ID 11177 does not recur and that queue manager processing continues.

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
