:orphan:

.. _winsyslog-event-id-11215:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11215: Debug error output was forwarded to the Windows Event Log.
   :event-id: 11215
   :event-product: WinSyslog
   :event-severity: Warning
   :event-component: Product runtime
   :event-reference: true

WinSyslog Event ID 11215: Debug error output was forwarded to the Windows Event Log
===================================================================================

Answer
------

A debug-level error message was emitted while Event Log warning forwarding was enabled.

Event details
-------------

- **Event ID:** ``11215``
- **Severity:** Warning
- **Component:** Product runtime
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** Debug error output was forwarded to the Windows Event Log.

Possible causes
---------------

- The configured Windows Event Log channel is unavailable, inaccessible, or contains an unreadable record.
- Publisher metadata, locale data, or the saved monitor state could not be processed.

Troubleshooting
---------------

#. Read the channel, provider, and record details included in the event.
#. Confirm the channel exists and the product service account can read it.
#. Check nearby Windows Event Log service errors, correct the channel or permissions issue, and retry.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11215 does not recur and that product runtime processing continues.

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

- :doc:`Event ID 11152 <event-id-11152>`
- :doc:`Event ID 11169 <event-id-11169>`
- :doc:`Event ID 11194 <event-id-11194>`
