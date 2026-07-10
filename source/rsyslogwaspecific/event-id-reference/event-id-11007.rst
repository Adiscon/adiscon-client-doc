:orphan:

.. _rsyslog-event-id-11007:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11007: Action configuration: required timer could not be created.
   :event-id: 11007
   :event-product: rsyslog Windows Agent
   :event-severity: Warning
   :event-component: Action configuration
   :event-reference: true

rsyslog Windows Agent Event ID 11007: Action configuration: required timer could not be created
===============================================================================================

Answer
------

The action configuration reported a warning condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11007``
- **Severity:** Warning
- **Component:** Action configuration
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Cactionconfigwritefile createtimer.

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

Repeat or monitor the affected operation and confirm that Event ID 11007 does not recur and that action configuration processing continues.

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

- :doc:`Event ID 11008 <event-id-11008>`
- :doc:`Event ID 11009 <event-id-11009>`
