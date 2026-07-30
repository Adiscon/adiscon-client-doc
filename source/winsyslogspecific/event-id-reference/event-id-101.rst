:orphan:

.. _winsyslog-event-id-101:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 101: The service was removed.
   :event-id: 101
   :event-product: WinSyslog
   :event-severity: Information
   :event-component: Windows service lifecycle
   :event-reference: true

WinSyslog Event ID 101: The service was removed
===============================================

Answer
------

The Windows service registration was removed.

Event details
-------------

- **Event ID:** ``101``
- **Severity:** Information
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The {service_name} service was removed.`

Possible causes
---------------

- A product uninstall or explicit service-remove operation deleted the Windows service registration.

Immediate checks
----------------

#. No repair is required when service removal was intended.
#. If removal was unexpected, identify the uninstall or administrative action that occurred at the same time.
#. Reinstall the service only after confirming that the product files and configuration should remain on this system.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the service registration is absent after an intended removal, or is present and starts normally after an authorized reinstall.

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

- :ref:`Event ID 100 <winsyslog-event-id-100>`
- :ref:`Event ID 102 <winsyslog-event-id-102>`
- :ref:`Event ID 103 <winsyslog-event-id-103>`
