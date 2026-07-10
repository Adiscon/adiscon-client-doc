:orphan:

.. _rsyslog-event-id-11058:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11058: Filter engine: regular expression initialization failed.
   :event-id: 11058
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Filter engine
   :event-reference: true

rsyslog Windows Agent Event ID 11058: Filter engine: regular expression initialization failed
=============================================================================================

Answer
------

The filter engine reported an error condition. The event detail identifies the affected operation and carries the specific runtime reason.

Event details
-------------

- **Event ID:** ``11058``
- **Severity:** Error
- **Component:** Filter engine
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** Cfilterlistentry cfilterlistentry.

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

Repeat or monitor the affected operation and confirm that Event ID 11058 does not recur and that filter engine processing continues.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry, including all event detail.
- The product name, exact version, service account, and event timestamp with time zone.
- A configuration export and debug log covering the same time window, with secrets removed.

Escalation
----------

If the event continues after the troubleshooting steps, collect the evidence above and contact Adiscon Support.
