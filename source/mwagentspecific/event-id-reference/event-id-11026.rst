:orphan:

.. _mwagent-event-id-11026:

.. meta::
   :description: Meaning and troubleshooting for MonitorWare Agent Event ID 11026: Configured action failed after its retries.
   :event-id: 11026
   :event-product: MonitorWare Agent
   :event-severity: Error
   :event-component: Rule engine action
   :event-reference: true

MonitorWare Agent Event ID 11026: Configured action failed after its retries
============================================================================

Answer
------

The named rule action raised an error. The product retried it according to the action settings and then skipped that action for the current event when no retry remained. The embedded error detail identifies the action-specific failure.

Event details
-------------

- **Event ID:** ``11026``
- **Severity:** Error
- **Component:** Rule engine action
- **Windows Event Log source:** ``AdisconMonitoreWareAgent``
- **Available since:** 26.07
- **Message pattern:** :spelling:ignore:`Error while applying an action - skipping action '{action_name}' (Try {attempt}). Error is '{error_detail}'.`

Possible causes
---------------

- A file action cannot open or write its destination because the path is unavailable, access is denied, the volume is full, or Windows reports a resource error. Windows error 5 indicates denied access, and error 112 indicates insufficient disk space.
- Windows error 8 or 1450 indicates that Windows could not provide enough memory or another system resource for the operation; the Event ID does not identify which resource was exhausted.
- A network action cannot reach its destination or encounters a DNS, socket, transport, TLS, or peer error.
- A database action fails under the service account because the provider, data source, authentication, permissions, or query is invalid or unavailable.
- Another action-specific dependency or configuration value is invalid or unavailable.

Immediate checks
----------------

#. Record the action name, attempt number, complete embedded error detail, and any Windows, Winsock, TLS, or provider error code.
#. Identify the configured action type and interpret the embedded error in that action's context; Event ID 11026 alone does not identify the failed dependency.
#. For Windows error 5 on a file destination, test both share and file-system permissions while running as the product service account.
#. For Windows error 112, check free space on the destination volume and verify the action's rotation and retention settings before deleting any files.
#. For Windows error 8 or 1450, capture system and product resource measurements plus neighboring events before restarting the service; do not assume that the action queue is the cause.
#. Test the affected destination using the product service account and the same path, endpoint, transport, or data source before changing unrelated settings.
#. Correct the action-specific cause, then send one uniquely identifiable test event through the affected rule.

Detailed procedures
-------------------

- :ref:`Interpret a Windows or Winsock error code <event-id-procedure-windows-interpret-error-code>` — Translate a numeric code without losing its operation or subsystem context.
- :ref:`Verify file paths, permissions, and free space <event-id-procedure-file-verify-path-permissions-and-disk-space>` — Check expansion, existence, ACLs, service-account context, and storage.
- :ref:`Diagnose log rotation and retention <event-id-procedure-file-diagnose-log-rotation>` — Verify trigger, names, handles, destination access, and retention.
- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>` — Verify DNS, selected address, routing, and TCP establishment.
- :ref:`Test an ODBC connection in the product context <event-id-procedure-database-test-odbc-connection>` — Verify ODBC provider, architecture, authentication, connectivity, and a minimal query.
- :ref:`Test an OLE DB connection in the product context <event-id-procedure-database-test-oledb-connection>` — Verify OLE DB provider, architecture, authentication, connectivity, and a minimal query.
- :ref:`Validate configuration and reload it safely <event-id-procedure-config-validate-and-reload>` — Back up, inspect, correct, and test the exact invalid configuration object.
- :ref:`Collect an Event ID and neighboring product events <event-id-procedure-evidence-collect-event-and-neighboring-events>` — Preserve the complete event and the product events immediately before and after it.
- :ref:`Export configuration and collect a bounded debug log <event-id-procedure-evidence-export-configuration-and-debug-log>` — Create a text configuration export and time-bounded debug capture, then disable debugging.

Verify the result
-----------------

Confirm that the uniquely identifiable test event reaches the affected action's destination, that no new Event ID 11026 is recorded for that action, and that any associated backlog decreases.

Evidence to collect
-------------------

- The complete Windows Application Event Log entry and neighboring product events, including the action name, attempt number, and embedded error detail.
- The product name, exact version, action type, service account, and event timestamp with time zone.
- A configuration export limited to the affected rule and action, plus a bounded debug log from the same interval.
- The relevant destination test and resource state, such as path access, free space, endpoint reachability, or database connection result.
- Remove passwords, tokens, license data, private keys, message payloads, personal data, and customer-identifying names, addresses, hostnames, domains, and network addresses before sharing evidence.

Escalation
----------

If the event continues after the detailed procedures, collect the listed evidence and contact Adiscon Support.

Related Event IDs
-----------------

- :ref:`Event ID 11014 <mwagent-event-id-11014>`
- :ref:`Event ID 11019 <mwagent-event-id-11019>`
- :ref:`Event ID 11021 <mwagent-event-id-11021>`
