:orphan:

.. _eventreporter-event-id-11164:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11164: Email action: invalid SMTP recipient address.
   :event-id: 11164
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Email action
   :event-reference: true

EventReporter Event ID 11164: Email action: invalid SMTP recipient address
==========================================================================

Answer
------

The email action reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11164``
- **Severity:** Error
- **Component:** Email action
- **Windows Event Log source:** ``Adiscon EvntSLog``
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

Repeat or monitor the affected operation and confirm that Event ID 11164 does not recur and that email action processing continues.

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

- :doc:`Event ID 11165 <event-id-11165>`
