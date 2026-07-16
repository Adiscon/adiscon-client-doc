:orphan:

.. _eventreporter-event-id-118:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 118: Product license status reminder.
   :event-id: 118
   :event-product: EventReporter
   :event-severity: Information
   :event-component: Licensing
   :event-reference: true

EventReporter Event ID 118: Product license status reminder
===========================================================

Answer
------

The service reports its current license mode at startup. The event detail states whether the product is in trial mode with remaining evaluation time or is running in a registered edition.

Event details
-------------

- **Event ID:** ``118``
- **Severity:** Information
- **Component:** Licensing
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The product reports its trial or registered license mode. Additional detail: {license_status_detail}`

Possible causes
---------------

- The service started in trial mode and reports the remaining evaluation period.
- The service started with a valid license and reports the active registered edition.

Immediate checks
----------------

#. Read the complete event detail to distinguish trial mode from registered mode.
#. No repair is required when the reported mode and edition are expected.
#. If the mode is unexpected, compare the running product and version with the displayed license status without copying license data.

Detailed procedures
-------------------

- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the service remains Running and that the reported license mode matches the intended product and edition.

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

- :ref:`Event ID 11005 <eventreporter-event-id-11005>`
- :ref:`Event ID 11043 <eventreporter-event-id-11043>`
- :ref:`Event ID 11044 <eventreporter-event-id-11044>`
