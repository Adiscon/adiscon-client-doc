:orphan:

.. _rsyslog-event-id-106:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 106: The service received an unsupported control request.
   :event-id: 106
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Windows service lifecycle
   :event-reference: true

rsyslog Windows Agent Event ID 106: The service received an unsupported control request
=======================================================================================

Answer
------

Windows delivered a service-control code that this product service does not implement. The requested control is ignored while supported service operations continue. This legacy event does not identify the control code.

Event details
-------------

- **Event ID:** ``106``
- **Severity:** Error
- **Component:** Windows service lifecycle
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** Current supported versions; original introduction not recorded
- **Message pattern:** :spelling:ignore:`The service received an unsupported request.`

Possible causes
---------------

- A management tool or script sent a control code that the product does not support.
- A monitoring or service-management integration used the wrong control operation.

Immediate checks
----------------

#. Use management-tool, script, and Service Control Manager logs from the event timestamp to identify the caller and control operation.
#. Change the caller to use supported start, stop, or other documented service operations.
#. Confirm that the service remains in its intended state after removing the unsupported request.

Detailed procedures
-------------------

- :ref:`Verify service state, dependencies, and service account <event-id-procedure-service-verify-state-and-account>` — Confirm service state, start mode, dependencies, account, and SCM errors.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Run the corrected management operation and confirm the intended service state without Event ID 106.

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
- :ref:`Event ID 102 <rsyslog-event-id-102>`
