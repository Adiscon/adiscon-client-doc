:orphan:

.. _eventreporter-event-id-11005:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11005: Configured feature is not licensed.
   :event-id: 11005
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Licensing
   :event-reference: true

EventReporter Event ID 11005: Configured feature is not licensed
================================================================

Answer
------

The product skipped the named input service, action, or advanced feature because the signed license does not include its required feature entitlement.

Event details
-------------

- **Event ID:** ``11005``
- **Severity:** Warning
- **Component:** Licensing
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`A configured module is not covered by the signed license feature entitlements. Additional detail: {event_detail}`

Possible causes
---------------

- The configuration enables a module that is not included in the installed edition or license.
- A configuration copied from another product or edition contains a feature that is unavailable here.
- The installed signed license does not match the intended product, version, or feature set.

Immediate checks
----------------

#. Record the module kind, module name, and required feature identifier from the complete event detail.
#. Confirm the running product, version, edition, and displayed license status without copying the license payload.
#. Either install an authorized license that includes the feature or disable the unsupported configured object, then reload the configuration.

Detailed procedures
-------------------

- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the intended module loads after configuration reload and performs one positive test without Event ID 11005 recurring.

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

- :ref:`Event ID 11043 <eventreporter-event-id-11043>`
- :ref:`Event ID 11044 <eventreporter-event-id-11044>`
- :ref:`Event ID 118 <eventreporter-event-id-118>`
