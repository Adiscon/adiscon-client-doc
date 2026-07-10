:orphan:

.. _rsyslog-event-id-11191:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11191: Service configuration: log rotation is not licensed.
   :event-id: 11191
   :event-product: rsyslog Windows Agent
   :event-severity: Information
   :event-component: Service configuration
   :event-reference: true

rsyslog Windows Agent Event ID 11191: Service configuration: log rotation is not licensed
=========================================================================================

Answer
------

The service configuration reported an informational condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11191``
- **Severity:** Information
- **Component:** Service configuration
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** This license does not include the logrotation feature.

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

Repeat or monitor the affected operation and confirm that Event ID 11191 does not recur and that service configuration processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

This event normally records state rather than a failure. Escalate only when the state was unexpected or the associated operation does not recover.

Related Event IDs
-----------------

- :doc:`Event ID 11183 <event-id-11183>`
- :doc:`Event ID 11184 <event-id-11184>`
- :doc:`Event ID 11185 <event-id-11185>`
