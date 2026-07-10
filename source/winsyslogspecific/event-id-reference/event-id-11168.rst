:orphan:

.. _winsyslog-event-id-11168:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11168: Runtime resource management: memory allocation failed.
   :event-id: 11168
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Runtime resource management
   :event-reference: true

WinSyslog Event ID 11168: Runtime resource management: memory allocation failed
===============================================================================

Answer
------

The runtime resource management reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11168``
- **Severity:** Error
- **Component:** Runtime resource management
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Pnhoutofmem.

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

Repeat or monitor the affected operation and confirm that Event ID 11168 does not recur and that runtime resource management processing continues.

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

- :doc:`Event ID 11167 <event-id-11167>`
