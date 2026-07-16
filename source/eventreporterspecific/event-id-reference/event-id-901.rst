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
- **Message pattern:** :spelling:ignore:`The product rejected a blocked license key during startup. Additional detail: {event_detail}`

Possible causes
---------------

- The installed key is on the product's blocked-key list and cannot authorize startup.
- License material intended for a different or superseded installation is still configured.

Immediate checks
----------------

#. Do not modify or repeatedly re-enter the blocked key.
#. Confirm the exact product and version, then obtain and install authorized replacement license material.
#. Start the service once and verify the reported license mode.

Detailed procedures
-------------------

- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the service reaches Running, reports the intended licensed mode, and does not emit Event ID 901 during startup.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11005 <eventreporter-event-id-11005>`
- :ref:`Event ID 11043 <eventreporter-event-id-11043>`
- :ref:`Event ID 11044 <eventreporter-event-id-11044>`
