.. _winsyslog-tutorial-database-logging:

Tutorial: Write Messages to Microsoft SQL Server
================================================

Use this tutorial when WinSyslog should store messages in Microsoft SQL Server
through an ODBC **System DSN** and the built-in default database schema.

Goal
----

At the end of this procedure, WinSyslog will write matching messages from a
ruleset into the default ``SystemEvents`` table in Microsoft SQL Server.

Why this tutorial uses the default schema
-----------------------------------------

This is the fastest supported path for a first production deployment. It keeps
the built-in field mapping, works with the **Create Database** button, and is
the safest choice if you later want Adiscon-compatible tooling or predictable
support behavior.

Prerequisites
-------------

- Microsoft SQL Server and SQL Server Management Studio (SSMS)
- Microsoft ODBC Driver 18 for SQL Server, or a compatible Microsoft SQL Server
  ODBC driver installed on the WinSyslog host
- Database credentials with permission to connect, insert rows, and create the
  default tables
- Access to the WinSyslog configuration client on the host where WinSyslog runs

Steps
-----

1. Create the target database in SQL Server.

   - Open SSMS and connect to the SQL Server instance that should receive the
     WinSyslog data.
   - Create an empty database for this integration.
   - Keep the database name available for the ODBC setup.

2. Create and test an ODBC **System DSN** on the WinSyslog host.

   - Open **Data Sources (ODBC)** on the WinSyslog host.
   - Create a new **System DSN** for SQL Server.
   - Select the Microsoft SQL Server driver that matches your environment, for
     example Microsoft ODBC Driver 18 for SQL Server.
   - Point the DSN to the SQL Server instance and database created in the
     previous step.
   - Complete the DSN wizard and use its built-in connection test.

3. Create or choose the WinSyslog ruleset whose messages should be stored.

4. Add a :doc:`Write to Database <../mwagentspecific/a-databaseoptions>`
   action to that ruleset.

5. Configure the database action.

   - Select the ODBC **System DSN** you created.
   - Enter the database credentials if the DSN or driver requires them.
   - Keep the default table name ``SystemEvents``.
   - Keep the default field list unless you intentionally need a custom schema.
   - Leave the SQL statement type at the normal ``INSERT`` path unless you have
     a verified SQL Server stored-procedure design.

   .. image:: ../images/a-odbcdatabase-connection.png
      :width: 100%
      :alt: Write to Database connection settings in the WinSyslog client

   *The connection tab is the main place to select the DSN, enter credentials,
   verify the connection, and create the default tables.*

6. Create the default database tables.

   - Use the action's **Verify Database** button first.
   - If the connection test succeeds, click **Create Database**.
   - Confirm that WinSyslog creates the default tables in the selected SQL
     Server database.

7. Save and apply the configuration.

   - Restart the WinSyslog service if your environment or workflow requires it.

8. Send or receive a test message that matches the ruleset.

9. Verify the inserted rows in SQL Server.

   - Open SSMS and query the ``SystemEvents`` table.
   - Confirm that the test message appears there.

   .. code-block:: sql

      SELECT TOP (10) *
      FROM dbo.SystemEvents;

Verification
------------

1. The ODBC **System DSN** test succeeds.
2. The action's **Verify Database** button succeeds.
3. The **Create Database** button creates the default tables.
4. A test message produces a new row in ``SystemEvents``.

Common issues
-------------

- The DSN was created as a user DSN instead of a **System DSN**.
- The DSN points to the wrong SQL Server instance or database.
- The SQL Server account can connect but does not have permission to create
  tables or insert rows.
- The default field list or table name was changed even though the goal is the
  default supported schema.
- Another tutorial path is actually needed because the destination must be an
  existing custom table.

Next step
---------

If the default schema path works and you want to keep it, continue with:

- :doc:`../mwagentspecific/a-databaseoptions`
- :doc:`tutorial-custom-database-integration`
- :doc:`producttour/store-and-forward`
- :doc:`faq/database-formats`
