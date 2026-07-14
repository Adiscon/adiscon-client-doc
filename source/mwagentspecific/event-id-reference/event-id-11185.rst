:orphan:

.. _mwagent-event-id-11185:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11185: No product input service is configured.
   :event-id: 11185
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Service configuration
   :event-reference: true

MonitorWare Agent Event ID 11185: No product input service is configured
========================================================================

Answer
------

The configuration contains no product input services. The Windows service can remain running, but it has no configured source from which to receive or collect events.

Event details
-------------

- **Event ID:** ``11185``
- **Severity:** Error
- **Component:** Service configuration
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`No input service is configured; the Windows service is running but cannot collect events.`

Possible causes
---------------

- All input services were deleted or disabled during configuration changes.
- A configuration import omitted the service objects.
- The service-count configuration is incomplete or damaged.

Immediate checks
----------------

#. Open the Configuration Client and inspect the Services tree.
#. Create or restore at least one intended input service and attach the correct ruleset.
#. Validate and reload the configuration.

Detailed procedures
-------------------

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Send an event to the restored input service and confirm that the product receives it without Event ID 11185 at startup.

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

- :ref:`Event ID 11183 <mwagent-event-id-11183>`
- :ref:`Event ID 11184 <mwagent-event-id-11184>`
- :ref:`Event ID 11186 <mwagent-event-id-11186>`
