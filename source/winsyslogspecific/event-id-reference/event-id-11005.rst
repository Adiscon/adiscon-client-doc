:orphan:

.. _winsyslog-event-id-11005:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11005: Configured feature is not licensed.
   :event-id: 11005
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Licensing
   :event-reference: true

WinSyslog Event ID 11005: Configured feature is not licensed
============================================================

Answer
------

The module or option is not loaded at startup.

Event details
-------------

- **Event ID:** ``11005``
- **Severity:** Warning
- **Component:** Licensing
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** A configured module is not covered by the signed license feature entitlements.

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

Repeat or monitor the affected operation and confirm that Event ID 11005 does not recur and that licensing processing continues.

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

- :doc:`Event ID 11043 <event-id-11043>`
- :doc:`Event ID 11044 <event-id-11044>`
- :doc:`Event ID 118 <event-id-118>`
