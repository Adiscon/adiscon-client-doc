:orphan:

.. _mwagent-event-id-11124:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11124: Serial Port Monitor: serial port operation raised an exception.
   :event-id: 11124
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Serial Port Monitor
   :event-reference: true

MonitorWare Agent Event ID 11124: Serial Port Monitor: serial port operation raised an exception
================================================================================================

Answer
------

The serial port monitor reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11124``
- **Severity:** Error
- **Component:** Serial Port Monitor
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Cinfosourceserialmonitor run.

Possible causes
---------------

- The runtime operation named in the event detail failed.
- A dependent Windows resource, configured endpoint, or product setting was unavailable or invalid.

Troubleshooting
---------------

#. Read the complete event detail and identify the operation, configured object, and Windows error code.
#. Check adjacent product events and the debug log for the first failure in the same time window.
#. Correct the reported configuration or dependency and repeat the operation.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11124 does not recur and that serial port monitor processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the troubleshooting steps, collect the evidence above and contact Adiscon Support.

Related Event IDs
-----------------

- :doc:`Event ID 11123 <event-id-11123>`
- :doc:`Event ID 11125 <event-id-11125>`
