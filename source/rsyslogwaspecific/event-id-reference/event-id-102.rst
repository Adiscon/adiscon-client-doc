:orphan:

.. _rsyslog-event-id-102:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 102: The service could not be removed.
   :event-id: 102
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Windows service lifecycle
   :event-reference: true

rsyslog Windows Agent Event ID 102: The service could not be removed
====================================================================

Answer
------

Windows rejected the request to delete the product service registration, so the service remains registered. This legacy event does not include the Windows error code.

Event details
-------------

- **Event ID:** ``102``
- **Severity:** Error
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The {service_name} service could not be removed.`

Possible causes
---------------

- The account performing removal lacks permission to delete the service.
- The service or another process still holds a Service Control Manager handle and Windows has marked it for deletion.
- The service name or registration state changed during removal.

Immediate checks
----------------

#. Record the event timestamp and inspect neighboring Service Control Manager and installer events for the underlying Windows error.
#. Confirm the current service registration and whether Windows already marked the service for deletion.
#. Close management tools that hold service handles, use an authorized administrator account, and retry the intended uninstall once.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the service registration is absent after the authorized removal and that Event ID 102 does not recur.

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

- :ref:`Event ID 100 <rsyslog-event-id-100>`
- :ref:`Event ID 101 <rsyslog-event-id-101>`
- :ref:`Event ID 103 <rsyslog-event-id-103>`
