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
- **Message pattern:** The product rejected a blocked license key during startup. Additional detail: {event_detail}

Possible causes
---------------

- The configured object is missing, invalid, unsupported by this product, or unavailable at runtime.
- Windows or a required provider returned the operation-specific error appended to the event.

Immediate checks
----------------

#. Identify the exact service, rule, filter, action, or setting named by the complete event detail.
#. Compare that object with the product reference and preserve the first related error in the same time window.
#. Correct only the identified setting or dependency, then run one controlled test.

Detailed procedures
-------------------

- :doc:`Verify product license and feature entitlement state <../../shared/troubleshooting/event-id/license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

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

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11005 <event-id-11005>`
- :doc:`Event ID 11043 <event-id-11043>`
- :doc:`Event ID 11044 <event-id-11044>`
