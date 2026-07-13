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

This procedure applies to EventReporter.

Prerequisites
-------------

- Use an account that can read the product configuration and Windows diagnostic state.
- Replace angle-bracket placeholders with values from the affected system.

Safety
------

- Do not place passwords in command history, logs, or support archives.
- Use a read-only query until connectivity is proven.

Configuration path
------------------

Configuration Client > the service, rule, or action named on the Event ID page.

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

- :ref:`EventReporter Event ID 11009 <eventreporter-event-id-11009>`
- :ref:`EventReporter Event ID 11010 <eventreporter-event-id-11010>`
- :ref:`EventReporter Event ID 11011 <eventreporter-event-id-11011>`
- :ref:`EventReporter Event ID 11026 <eventreporter-event-id-11026>`
- :ref:`EventReporter Event ID 11029 <eventreporter-event-id-11029>`
- :ref:`EventReporter Event ID 11030 <eventreporter-event-id-11030>`
- :ref:`EventReporter Event ID 11066 <eventreporter-event-id-11066>`
- :ref:`EventReporter Event ID 11067 <eventreporter-event-id-11067>`
- :ref:`EventReporter Event ID 11069 <eventreporter-event-id-11069>`
- :ref:`EventReporter Event ID 11070 <eventreporter-event-id-11070>`
- :ref:`EventReporter Event ID 11173 <eventreporter-event-id-11173>`


Related procedures
------------------

- :ref:`Resolve a destination and test its TCP port <event-id-procedure-network-resolve-host-and-test-tcp-port>`
- :ref:`Diagnose an action backlog or disk queue <event-id-procedure-queue-diagnose-backlog-and-disk-queue>`
