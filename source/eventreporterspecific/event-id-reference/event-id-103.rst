:orphan:

.. _eventreporter-event-id-103:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 103: The service control handler could not be installed.
   :event-id: 103
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Windows service lifecycle
   :event-reference: true

EventReporter Event ID 103: The service control handler could not be installed
==============================================================================

Answer
------

The service process could not register its control handler with Windows and terminates startup before normal service controls can be processed.

Event details
-------------

- **Event ID:** ``103``
- **Severity:** Error
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The control handler could not be installed.`

Possible causes
---------------

- The executable was started outside the Service Control Manager instead of as the registered Windows service.
- Windows rejected handler registration because the service process or registration state is invalid.
- A Windows service-control failure occurred during very early startup.

Immediate checks
----------------

#. Start the product through Windows Services or Start-Service, not by launching the service executable interactively.
#. Check neighboring Service Control Manager events and the registered executable path.
#. Repair the product installation if the service registration points to the wrong executable, then perform one controlled start.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that Windows reports the service as Running and that normal stop and start controls work without Event ID 103.

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

- :ref:`Event ID 100 <eventreporter-event-id-100>`
- :ref:`Event ID 101 <eventreporter-event-id-101>`
- :ref:`Event ID 102 <eventreporter-event-id-102>`
