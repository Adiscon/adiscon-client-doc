:orphan:

.. _eventreporter-event-id-901:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 901: Blocked license key rejected.
   :event-id: 901
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Licensing
   :event-reference: true

EventReporter Event ID 901: Blocked license key rejected
========================================================

Answer
------

The product service does not start with the blocked key.

Event details
-------------

- **Event ID:** ``901``
- **Severity:** Error
- **Component:** Licensing
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** The product rejected a blocked license key during startup.

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

Repeat or monitor the affected operation and confirm that Event ID 901 does not recur and that licensing processing continues.

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
- :doc:`Event ID 11044 <event-id-11044>`
