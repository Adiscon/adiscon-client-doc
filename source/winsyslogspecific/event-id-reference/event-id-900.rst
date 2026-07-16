:orphan:

.. _winsyslog-event-id-900:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 900: Invalid license key rejected.
   :event-id: 900
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Licensing
   :event-reference: true

WinSyslog Event ID 900: Invalid license key rejected
====================================================

Answer
------

The WinSyslog service does not start with the rejected key.

Event details
-------------

- **Event ID:** ``900``
- **Severity:** Error
- **Component:** Licensing
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`WinSyslog rejected an invalid license key during startup. Additional detail: {event_detail}`

Possible causes
---------------

- The installed key is invalid, altered, or not issued for this WinSyslog product and version.
- License material was copied incompletely or placed in the wrong product configuration.

Immediate checks
----------------

#. Confirm the running WinSyslog version and displayed license status without copying or editing the key.
#. Replace the rejected material with the authorized license issued for this product and version.
#. Start WinSyslog once and verify the reported license mode.

Detailed procedures
-------------------

- :ref:`Verify product license and feature entitlement state <event-id-procedure-license-verify-license-state>` — Confirm product, version, validity, edition, and required feature without exposing license data.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that WinSyslog reaches Running, reports the intended licensed mode, and does not emit Event ID 900 during startup.

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

- :ref:`Event ID 11005 <winsyslog-event-id-11005>`
- :ref:`Event ID 11043 <winsyslog-event-id-11043>`
- :ref:`Event ID 11044 <winsyslog-event-id-11044>`
