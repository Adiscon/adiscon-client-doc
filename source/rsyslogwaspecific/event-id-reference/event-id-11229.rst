:orphan:

.. _rsyslog-event-id-11229:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11229: Message Ringbuffer action is not registered.
   :event-id: 11229
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Message Ringbuffer action
   :event-reference: true

rsyslog Windows Agent Event ID 11229: Message Ringbuffer action is not registered
=================================================================================

Answer
------

The action could not retain processed messages because no named buffer is registered for its configured id.

Event details
-------------

- **Event ID:** ``11229``
- **Severity:** Error
- **Component:** Message Ringbuffer action
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.08
- **Message pattern:** :spelling:ignore:`A Message Ringbuffer action could not store messages because its buffer is not registered. Additional detail: {event_detail}`

Possible causes
---------------

- szRingBufferId is empty, invalid, or reserved (diagnostics).
- The service configuration was loaded before the process-wide ringbuffer registry was available.
- The Message Ringbuffer action is disabled or not present in the running configuration.

Immediate checks
----------------

#. Confirm szRingBufferId is set to a URL-safe id of 1..64 characters and is not diagnostics.
#. Save the configuration and restart or reload the service.
#. Query GET v1/ringbuffers on the metrics listener and confirm the configured id is listed.

Detailed procedures
-------------------

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Process a message through the action and confirm Event ID 11229 does not recur and the Metrics ringbuffer endpoints return the retained message.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry.
- The action configuration including szRingBufferId, and a Metrics v1/ringbuffers response.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.
