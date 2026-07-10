:orphan:

.. _rsyslog-event-id-11186:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11186: Service configuration: trial period expired.
   :event-id: 11186
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Service configuration
   :event-reference: true

rsyslog Windows Agent Event ID 11186: Service configuration: trial period expired
=================================================================================

Answer
------

The service configuration reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11186``
- **Severity:** Error
- **Component:** Service configuration
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Servicemanager.

Possible causes
---------------

- The service received an invalid setting or could not initialize a configured component.
- Windows denied a required service, registry, file, or operating-system operation.

Troubleshooting
---------------

#. Read this event together with adjacent product events that contain the detailed failure.
#. Validate the recently changed configuration and the product service account permissions.
#. Correct the reported setting or operating-system condition, then restart or reload the service.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11186 does not recur and that service configuration processing continues.

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

- :doc:`Event ID 11183 <event-id-11183>`
- :doc:`Event ID 11184 <event-id-11184>`
- :doc:`Event ID 11185 <event-id-11185>`
