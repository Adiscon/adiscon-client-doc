:orphan:

.. _rsyslog-event-id-11165:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11165: Email action: SMTP recipient address is missing.
   :event-id: 11165
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Email action
   :event-reference: true

rsyslog Windows Agent Event ID 11165: Email action: SMTP recipient address is missing
=====================================================================================

Answer
------

The email action reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11165``
- **Severity:** Error
- **Component:** Email action
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Cmailrcptlist setrecipients.

Possible causes
---------------

- The runtime operation named in the event detail failed.
- A dependent Windows resource, configured endpoint, or product setting was unavailable or invalid.

Troubleshooting
---------------

#. Read the complete event detail and identify the operation, configured object, and Windows error code.
#. Check adjacent product events and the debug log for the first failure in the same time window.
#. Correct the reported configuration or dependency and repeat the operation.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11165 does not recur and that email action processing continues.

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

- :doc:`Event ID 11164 <event-id-11164>`
