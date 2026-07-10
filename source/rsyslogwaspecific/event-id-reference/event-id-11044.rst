:orphan:

.. _rsyslog-event-id-11044:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11044: Licensing: licensed client limit exceeded.
   :event-id: 11044
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Licensing
   :event-reference: true

rsyslog Windows Agent Event ID 11044: Licensing: licensed client limit exceeded
===============================================================================

Answer
------

The licensing reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11044``
- **Severity:** Error
- **Component:** Licensing
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Client license limit exceeded.

Possible causes
---------------

- The installed license file is missing, invalid, blocked, expired, or does not cover the configured feature.

Troubleshooting
---------------

#. Read the license or feature name included in the event detail.
#. Verify that the correct current license file is installed for this product and system.
#. Apply the correct license file and restart or reload the product configuration.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11044 does not recur and that licensing processing continues.

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

- :doc:`Event ID 11005 <event-id-11005>`
- :doc:`Event ID 11043 <event-id-11043>`
- :doc:`Event ID 118 <event-id-118>`
