:orphan:

.. _winsyslog-event-id-100:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 100: The service was installed.
   :event-id: 100
   :event-product: WinSyslog
   :event-severity: Information
   :event-component: Windows service lifecycle
   :event-reference: true

WinSyslog Event ID 100: The service was installed
=================================================

Answer
------

The Windows service registration completed.

Event details
-------------

- **Event ID:** ``100``
- **Severity:** Information
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The {service_name} service was installed.`

Possible causes
---------------

- A product installation or explicit service-install operation registered the Windows service.

Immediate checks
----------------

#. No repair is required when service installation was intended.
#. If the registration was unexpected, identify the installation or administrative action that occurred at the same time.
#. Verify the registered service name, executable path, start mode, and service account before starting it.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that Windows reports the intended service registration and that the service can enter the Running state.

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

- :ref:`Event ID 101 <winsyslog-event-id-101>`
- :ref:`Event ID 102 <winsyslog-event-id-102>`
- :ref:`Event ID 103 <winsyslog-event-id-103>`
