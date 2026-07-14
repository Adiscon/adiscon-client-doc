:orphan:

.. _eventreporter-event-id-11173:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11173: An event failed while the main queue applied its rules.
   :event-id: 11173
   :event-product: EventReporter
   :event-severity: Error
   :event-component: Main message queue
   :event-reference: true

EventReporter Event ID 11173: An event failed while the main queue applied its rules
====================================================================================

Answer
------

A normal diagnostic exception escaped while a queue worker applied the selected ruleset to one event. The product records the error and finishes that event instead of leaving it in the in-memory queue.

Event details
-------------

- **Event ID:** ``11173``
- **Severity:** Error
- **Component:** Main message queue
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Queue rule-processing error: {error_detail}`

Possible causes
---------------

- A filter, action, or property operation raised a diagnostic exception.
- The event or ruleset contains an invalid value.
- A destination or provider used during rule processing failed.

Immediate checks
----------------

#. Use the embedded error and neighboring action events to identify the failing rule operation.
#. Preserve the affected ruleset and a sanitized sample event, then reproduce with one controlled event.
#. Correct the identified operation and verify subsequent queue processing.

Detailed procedures
-------------------

- :ref:`Interpret a Windows or Winsock error code <event-id-procedure-windows-interpret-error-code>` — Translate a numeric code without losing its operation or subsystem context.
- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Test an ODBC connection in the product context <event-id-procedure-database-test-odbc-connection>` — Verify ODBC provider, architecture, authentication, connectivity, and a minimal query.
- :ref:`Test an OLE DB connection in the product context <event-id-procedure-database-test-oledb-connection>` — Verify OLE DB provider, architecture, authentication, connectivity, and a minimal query.
- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that controlled events complete the ruleset and queue depth decreases without Event ID 11173.

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

- :ref:`Event ID 11170 <eventreporter-event-id-11170>`
- :ref:`Event ID 11171 <eventreporter-event-id-11171>`
- :ref:`Event ID 11172 <eventreporter-event-id-11172>`
