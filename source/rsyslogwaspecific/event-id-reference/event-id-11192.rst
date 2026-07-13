:orphan:

.. _rsyslog-event-id-11192:

.. meta::
   :description: Meaning and troubleshooting for rsyslog Windows Agent Event ID 11192: No configured product input service could be started.
   :event-id: 11192
   :event-product: rsyslog Windows Agent
   :event-severity: Error
   :event-component: Service startup
   :event-reference: true

rsyslog Windows Agent Event ID 11192: No configured product input service could be started
==========================================================================================

Answer
------

The product finished loading the configured input services but none started successfully. It marks the Windows service to stop because it cannot collect events.

Event details
-------------

- **Event ID:** ``11192``
- **Severity:** Error
- **Component:** Service startup
- **Windows Event Log source:** ``RSyslogWindowsAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`No input service could be started; the product service will stop.`

Possible causes
---------------

- Every input service has an invalid or missing dependency such as its ruleset, binding, certificate, or source.
- The service account lacks permissions required by all configured inputs.
- The configuration is incompatible, incomplete, or damaged.

Immediate checks
----------------

#. Review the earlier the product events from the same startup and identify the first service-specific failure.
#. Correct that underlying service failure instead of repeatedly restarting the Windows service.
#. Validate the configuration and perform one controlled start.

Detailed procedures
-------------------

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that at least one intended input service starts, receives a controlled event, and the product Windows service remains running.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11183 <rsyslog-event-id-11183>`
- :ref:`Event ID 11184 <rsyslog-event-id-11184>`
- :ref:`Event ID 11185 <rsyslog-event-id-11185>`
