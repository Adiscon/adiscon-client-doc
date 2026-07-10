:orphan:

.. _event-id-procedure-database-test-odbc-connection:

.. meta::
   :description: Verify ODBC provider, architecture, authentication, connectivity, and a minimal query.
   :procedure-id: database.test-odbc-connection
   :procedure-reference: true

Test an ODBC connection in the product context
==============================================

When to use this procedure
--------------------------

Use for ODBC actions and database-monitor events.

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

      Get-OdbcDsn -Name '<DSN_NAME>' | Format-List Name,DsnType,Platform,DriverName

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

   - WinSyslog Event ID 11010
   - WinSyslog Event ID 11011
   - WinSyslog Event ID 11029
   - WinSyslog Event ID 11030
   - WinSyslog Event ID 11066
   - WinSyslog Event ID 11067
   - WinSyslog Event ID 11069
   - WinSyslog Event ID 11070

.. only:: eventreporter

   - EventReporter Event ID 11010
   - EventReporter Event ID 11011
   - EventReporter Event ID 11029
   - EventReporter Event ID 11030
   - EventReporter Event ID 11066
   - EventReporter Event ID 11067
   - EventReporter Event ID 11069
   - EventReporter Event ID 11070

.. only:: mwagent

   - MonitorWare Agent Event ID 11010
   - MonitorWare Agent Event ID 11011
   - MonitorWare Agent Event ID 11029
   - MonitorWare Agent Event ID 11030
   - MonitorWare Agent Event ID 11066
   - MonitorWare Agent Event ID 11067
   - MonitorWare Agent Event ID 11069
   - MonitorWare Agent Event ID 11070

.. only:: rsyslog

   - rsyslog Windows Agent Event ID 11010
   - rsyslog Windows Agent Event ID 11011
   - rsyslog Windows Agent Event ID 11029
   - rsyslog Windows Agent Event ID 11030
   - rsyslog Windows Agent Event ID 11066
   - rsyslog Windows Agent Event ID 11067
   - rsyslog Windows Agent Event ID 11069
   - rsyslog Windows Agent Event ID 11070


Related procedures
------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>`
- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>`
