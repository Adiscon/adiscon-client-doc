:orphan:

.. _mwagent-event-id-11151:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11151: Event Log Monitor V2 service: Windows Event Log operation failed.
   :event-id: 11151
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Event Log Monitor V2 service
   :event-reference: true

MonitorWare Agent Event ID 11151: Event Log Monitor V2 service: Windows Event Log operation failed
==================================================================================================

Answer
------

Event Log Monitor V2 service: Windows Event Log operation failed. The product recorded this while processing event log monitor v2 service; the appended event detail identifies the affected object, operation, or provider error.

Event details
-------------

- **Event ID:** ``11151``
- **Severity:** Error
- **Component:** Event Log Monitor V2 service
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** Event Log Monitor V2 service: Windows Event Log operation failed. Additional detail: {event_detail}

Possible causes
---------------

- The configured Windows Event Log channel is missing, disabled, inaccessible, or no longer matches the saved collection position.
- The service account cannot read the channel or provider metadata, or the channel was cleared or recreated.

Immediate checks
----------------

#. Identify the exact channel, collection mode, saved position, and service account.
#. Confirm that Windows reports the channel enabled and readable in the service-account context.
#. Use one safe test event to verify collection before resetting any saved position.

Detailed procedures
-------------------

- :doc:`Verify Event Log channel access and bookmark state <../../shared/troubleshooting/event-id/eventlog-verify-channel-access-and-bookmark>` — Confirm channel existence, enablement, account access, and collection position.
- :doc:`Collect an Event ID and neighboring product events <../../shared/troubleshooting/event-id/evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :doc:`Export configuration and collect a bounded debug log <../../shared/troubleshooting/event-id/evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Repeat or monitor the affected operation and confirm that Event ID 11151 does not recur and that event log monitor v2 service processing continues.

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

- :doc:`Event ID 11147 <event-id-11147>`
- :doc:`Event ID 11148 <event-id-11148>`
- :doc:`Event ID 11149 <event-id-11149>`
