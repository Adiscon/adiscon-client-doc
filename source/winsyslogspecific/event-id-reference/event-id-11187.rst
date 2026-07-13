:orphan:

.. _winsyslog-event-id-11187:

.. meta::
   :description: Meaning and troubleshooting for WinSyslog Event ID 11187: A configured input service type is not recognized.
   :event-id: 11187
   :event-product: WinSyslog
   :event-severity: Error
   :event-component: Service configuration
   :event-reference: true

WinSyslog Event ID 11187: A configured input service type is not recognized
===========================================================================

Answer
------

The configuration contains an input-service type that the installed product build cannot create. The product ignores that service object and continues loading the remaining services.

Event details
-------------

- **Event ID:** ``11187``
- **Severity:** Error
- **Component:** Service configuration
- **Windows Event Log source:** ``AdisconWinSyslog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Unknown service type {service_type} was found and ignored.`

Possible causes
---------------

- The configuration came from a newer or incompatible product version.
- A manual configuration edit supplied an invalid service type.
- The service object is incomplete or damaged.

Immediate checks
----------------

#. Export and back up the current configuration.
#. Identify the ignored service and compare its type with services supported by the installed product version.
#. Recreate it with a supported type or install the intended compatible version, then reload.

Detailed procedures
-------------------

- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the recreated input service starts and receives a controlled event without Event ID 11187.

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

- :ref:`Event ID 11183 <winsyslog-event-id-11183>`
- :ref:`Event ID 11184 <winsyslog-event-id-11184>`
- :ref:`Event ID 11185 <winsyslog-event-id-11185>`
