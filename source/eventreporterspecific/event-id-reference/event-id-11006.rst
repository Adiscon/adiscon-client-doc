:orphan:

.. _eventreporter-event-id-11006:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11006: Call Ruleset action could not find its target ruleset.
   :event-id: 11006
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Call Ruleset action
   :event-reference: true

EventReporter Event ID 11006: Call Ruleset action could not find its target ruleset
===================================================================================

Answer
------

The action references a ruleset that was not present when the product initialized the action. Events reaching this action cannot be processed by the missing target ruleset.

Event details
-------------

- **Event ID:** ``11006``
- **Severity:** Error
- **Component:** Call Ruleset action
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`The Call Ruleset action could not find configured ruleset '{ruleset_name}'.`

Possible causes
---------------

- The target ruleset was renamed or deleted.
- The action contains an empty, misspelled, or stale ruleset name.
- A configuration import omitted the referenced ruleset.

Immediate checks
----------------

#. Open the affected Call Ruleset action and record its target ruleset name.
#. Confirm that a ruleset with that exact name exists in the same configuration.
#. Correct the reference or restore the missing ruleset, validate the configuration, and reload it.

Detailed procedures
-------------------

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Send a uniquely identifiable test event through the calling rule and confirm that the target ruleset processes it without another Event ID 11006.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events from the same time window.
- The exact product version, affected service or action name, and event timestamp with time zone.
- The affected configuration object and a bounded debug log covering one controlled reproduction.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.
