:orphan:

.. _mwagent-event-id-11019:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11019: Syslog Queue action has no queue name.
   :event-id: 11019
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Syslog Queue action
   :event-reference: true

MonitorWare Agent Event ID 11019: Syslog Queue action has no queue name
=======================================================================

Answer
------

The product cannot initialize the Syslog Queue action because its required queue name is empty.

Event details
-------------

- **Event ID:** ``11019``
- **Severity:** Error
- **Component:** Syslog Queue action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Failed to initialize Syslog Queue action: the configured queue name is empty.`

Possible causes
---------------

- The queue name was never configured.
- A configuration import or manual file edit removed the queue name.
- The action configuration is incomplete.

Immediate checks
----------------

#. Open the affected Syslog Queue action.
#. Configure a non-empty queue name that matches the intended queue consumer.
#. Validate and reload the configuration.

Detailed procedures
-------------------

- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>` — Identify why queued work is not draining while preserving data.
- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Send a controlled event through the action and confirm that it enters the named queue without another Event ID 11019.

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

- :ref:`Event ID 11014 <mwagent-event-id-11014>`
- :ref:`Event ID 11021 <mwagent-event-id-11021>`
- :ref:`Event ID 11022 <mwagent-event-id-11022>`
