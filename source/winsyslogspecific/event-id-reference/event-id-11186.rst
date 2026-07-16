:orphan:

.. _winsyslog-event-id-11186:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11186: The trial expired and the service was disabled.
   :event-id: 11186
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Licensing
   :event-reference: true

WinSyslog Event ID 11186: The trial expired and the service was disabled
========================================================================

Answer
------

The evaluation period ended without a valid license, and this product does not permit continued free operation. The product keeps the configuration but does not start its input services.

Event details
-------------

- **Event ID:** ``11186``
- **Severity:** Error
- **Component:** Licensing
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`ServiceManager. Trial expired. The service is disabled and the existing configuration remains intact. Additional detail: {event_detail}`

Possible causes
---------------

- The evaluation period expired and no valid product license is installed.
- The installed license is invalid for the running product or version.

Immediate checks
----------------

#. Confirm the exact product, version, and displayed license state without copying license data.
#. Install the authorized license for this product and version; do not edit signed license content.
#. Start the service and verify that its configured inputs load and process one controlled test.

Detailed procedures
-------------------

- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the Windows service remains running, at least one configured input starts, and Event ID 11186 does not recur.

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

- :ref:`Event ID 11183 <winsyslog-event-id-11183>`
- :ref:`Event ID 11184 <winsyslog-event-id-11184>`
- :ref:`Event ID 11185 <winsyslog-event-id-11185>`
