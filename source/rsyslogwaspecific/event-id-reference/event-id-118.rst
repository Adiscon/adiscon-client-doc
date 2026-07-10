:orphan:

.. _rsyslog-event-id-118:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 118: Trial mode reminder.
   :event-id: 118
   :event-product: rsyslog Windows Agent
   :event-severity: Information
   :event-component: Licensing
   :event-reference: true

rsyslog Windows Agent Event ID 118: Trial mode reminder
=======================================================

Answer
------

Trial limits and expiration apply to the running product.

Event details
-------------

- **Event ID:** ``118``
- **Severity:** Information
- **Component:** Licensing
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** The product is running in trial mode; the event detail contains the remaining trial information.

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

Repeat or monitor the affected operation and confirm that Event ID 118 does not recur and that licensing processing continues.

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

- :doc:`Event ID 11005 <event-id-11005>`
- :doc:`Event ID 11043 <event-id-11043>`
- :doc:`Event ID 11044 <event-id-11044>`
