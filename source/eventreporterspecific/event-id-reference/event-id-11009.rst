:orphan:

.. _eventreporter-event-id-11009:

.. meta::
   :description: Meaning and troubleshooting for EventReporter Event ID 11009: A queued action message could not be delivered.
   :event-id: 11009
   :event-product: EventReporter
   :event-severity: Warning
   :event-component: Action disk queue
   :event-reference: true

EventReporter Event ID 11009: A queued action message could not be delivered
============================================================================

Answer
------

The product read a message from an action disk queue, but the destination operation failed. The queue read position is restored so the message can be retried rather than silently skipped.

Event details
-------------

- **Event ID:** ``11009``
- **Severity:** Warning
- **Component:** Action disk queue
- **Windows Event Log source:** ``Adiscon EvntSLog``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Error sending message '{error_detail}' - error '{error_code}'`

Possible causes
---------------

- The action destination is unavailable or rejecting the operation.
- A network, provider, file, or service dependency used by the queued action failed.
- The action configuration or credentials no longer match the destination.

Immediate checks
----------------

#. Use the action name and embedded error to identify the action type and failed destination.
#. Confirm that the queued message remains available and record the oldest queued-item time.
#. Test the destination in the product service-account context, correct the action-specific failure, and allow queued delivery to resume.

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

Confirm that the action queue drains, the destination receives a controlled test event, and Event ID 11009 does not recur.

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

- :ref:`Event ID 11007 <eventreporter-event-id-11007>`
- :ref:`Event ID 11008 <eventreporter-event-id-11008>`
