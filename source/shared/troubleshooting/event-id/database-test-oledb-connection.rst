:orphan:

.. _event-id-procedure-database-test-oledb-connection:

.. meta::
   :description: Verify OLE DB provider, architecture, authentication, connectivity, and a minimal query.
   :procedure-id: database.test-oledb-connection
   :procedure-reference: true

Test an OLE DB connection in the product context
================================================

When to use this procedure
--------------------------

Use for OLE DB actions and database-monitor events.

Applies to
----------

Prerequisites
-------------

.. only:: eventreporter

   This procedure applies to EventReporter.

.. only:: winsyslog or winsyslog_j

   This procedure applies to WinSyslog.

.. only:: mwagent

   This procedure applies to MonitorWare Agent.

.. only:: rsyslog

   This procedure applies to rsyslog Windows Agent.

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Do not place passwords in command history, logs, or support archives.
- Use a read-only query until connectivity is proven.

Configuration paths
-------------------

.. only:: eventreporter

   **EventReporter:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: winsyslog or winsyslog_j

   **WinSyslog:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: mwagent

   **MonitorWare Agent:** Configuration Client > the service, rule, or action named on the Event ID page.

.. only:: rsyslog

   **rsyslog Windows Agent:** Configuration Client > the service, rule, or action named on the Event ID page.

Procedure
---------

#. Record provider/DSN, server, database, authentication mode, service account, and redacted connection fields.

   **Expected result:** The affected object and its effective settings are identified.

   **If it fails:** Return to the complete Event Log detail and configuration export before changing settings.

#. Run the native Windows checks below from the affected product host.

   .. code-block:: powershell

      $cn=[Data.OleDb.OleDbConnection]::new('<REDACTED_TEST_CONNECTION_STRING>'); $cn.Open(); $cn.State; $cn.Close()

   **Expected result:** The provider exists in the correct bitness and a redacted test connection opens successfully.

   **If it fails:** Use the provider error to correct driver, DNS, port, database, TLS, credentials, or permissions.

#. Perform one uniquely identifiable product test through the same service, rule, or action.

   **Expected result:** The intended destination records the test exactly once.

   **If it fails:** Collect the first new product event and bounded debug output; do not change unrelated settings.

Verify the result
-----------------

Repeat the affected operation, confirm its positive output, and verify that queues, collection positions, or remote delivery continue normally.

Evidence to collect
-------------------

- The complete Event Log entry and neighboring product events with timestamps.
- The command output, relevant configuration export, and bounded debug log from the same interval.

Related Event IDs
-----------------

.. only:: winsyslog or winsyslog_j

   - WinSyslog Event ID 11012
   - WinSyslog Event ID 11013
   - WinSyslog Event ID 11031
   - WinSyslog Event ID 11032
   - WinSyslog Event ID 11066
   - WinSyslog Event ID 11067
   - WinSyslog Event ID 11069
   - WinSyslog Event ID 11070
   - WinSyslog Event ID 11166

.. only:: eventreporter

   - EventReporter Event ID 11012
   - EventReporter Event ID 11013
   - EventReporter Event ID 11031
   - EventReporter Event ID 11032
   - EventReporter Event ID 11066
   - EventReporter Event ID 11067
   - EventReporter Event ID 11069
   - EventReporter Event ID 11070
   - EventReporter Event ID 11166

.. only:: mwagent

   - MonitorWare Agent Event ID 11012
   - MonitorWare Agent Event ID 11013
   - MonitorWare Agent Event ID 11031
   - MonitorWare Agent Event ID 11032
   - MonitorWare Agent Event ID 11066
   - MonitorWare Agent Event ID 11067
   - MonitorWare Agent Event ID 11069
   - MonitorWare Agent Event ID 11070
   - MonitorWare Agent Event ID 11166

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11012
   - rsyslog Windows Agent Event ID 11013
   - rsyslog Windows Agent Event ID 11031
   - rsyslog Windows Agent Event ID 11032
   - rsyslog Windows Agent Event ID 11066
   - rsyslog Windows Agent Event ID 11067
   - rsyslog Windows Agent Event ID 11069
   - rsyslog Windows Agent Event ID 11070
   - rsyslog Windows Agent Event ID 11166


Related procedures
------------------

- :doc:`Resolve a destination and test its TCP port <network-resolve-host-and-test-tcp-port>`
- :doc:`Diagnose an action backlog or disk queue <queue-diagnose-backlog-and-disk-queue>`
