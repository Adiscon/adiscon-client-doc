.. _winsyslog-tutorial-database-logging:

Quick Start: Write Syslog Messages to Microsoft SQL Server
==========================================================

Use this tutorial when you want a hands-on setup that turns one known syslog
message into rows in Microsoft SQL Server with a reproducible table and field
mapping.

Question
--------

How do I quickly write WinSyslog syslog messages to Microsoft SQL Server?

Answer
------

Create one ODBC **System DSN**, point WinSyslog at one SQL Server table, map
the syslog properties to the target columns, send one test message, and verify
the row in SQL Server. This tutorial uses a fixed demo database so you can
reproduce the result immediately.

At a glance
-----------

- Database: ``WinSyslogDemo``
- Table: ``dbo.WinSyslogIncoming``
- DSN: ``WinSyslogDemo``
- Input: one RFC 5424 syslog message
- Output: one row with raw and structured message columns

Goal
----

At the end of this procedure, WinSyslog will:

- receive a test syslog message
- write that message into Microsoft SQL Server through an ODBC
  **System DSN**
- store both the raw message and a structured view of the same event in a
  simple database table

What you will build
-------------------

- a SQL Server database named ``WinSyslogDemo``
- a table named ``dbo.WinSyslogIncoming``
- an ODBC **System DSN** named ``WinSyslogDemo``
- a WinSyslog ruleset with one **Write to Database** action
- a repeatable test row you can query in SQL Server

Sample message and output
-------------------------

This quick start uses a single RFC 5424-style syslog message so the database
row is easy to recognize.

Sample input message:

.. code-block:: text

   <134>1 2026-04-01T08:15:00Z fw01 sshd 1234 ID47 - Accepted password for alice from 192.0.2.10 port 55221

The example table stores the same event twice:

- once as the raw message
- once as the parsed message text and header fields

The mapping is intentionally small and explicit:

- ``timereported`` becomes ``received_at``
- ``source`` becomes ``source_host``
- ``syslogfacility_text`` becomes ``facility_text``
- ``syslogpriority_text`` becomes ``severity_text``
- ``syslogappname`` becomes ``app_name``
- ``rawsyslogmsg`` becomes ``raw_message``
- ``msgPropertyDescribed`` becomes ``message_text``

Expected output in SQL Server:

.. code-block:: text

   received_at   = 2026-04-01 08:15:00
   source_host   = fw01
   facility_text = Local0
   severity_text = Informational
   app_name      = sshd
   raw_message   = <134>1 2026-04-01T08:15:00Z fw01 sshd 1234 ID47 - Accepted password for alice from 192.0.2.10 port 55221
   message_text  = Accepted password for alice from 192.0.2.10 port 55221

Prerequisites
-------------

- Microsoft SQL Server and SQL Server Management Studio (SSMS)
- Microsoft ODBC Driver 18 for SQL Server, or a compatible Microsoft SQL Server
  ODBC driver installed on the WinSyslog host
- Database credentials with permission to connect, insert rows, and create
  tables
- Access to the WinSyslog configuration client on the host where WinSyslog runs

Required downloads
------------------

If you do not already have the Microsoft components installed, use these
official download pages before you start the tutorial:

- `Microsoft SQL Server downloads`_

  Use the Express edition on this page if you need a free local SQL Server
  instance for the demo database.

- `SQL Server Management Studio`_

  Use SSMS if you want to create the database and table in a GUI. The article
  includes the current direct download link.

- `Microsoft ODBC Driver for SQL Server`_

  WinSyslog writes to SQL Server through ODBC, so install the driver that
  matches the WinSyslog host architecture.

.. _Microsoft SQL Server downloads: https://www.microsoft.com/en-US/sql-server/sql-server-downloads
.. _SQL Server Management Studio: https://learn.microsoft.com/en-us/ssms/install/install
.. _Microsoft ODBC Driver for SQL Server: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17

Steps
-----

1. Create the target database and table in SQL Server.

   - Open SSMS and connect to the SQL Server instance that should receive the
     WinSyslog data.
   - Run the following SQL script to create the demo database and table:

   .. literalinclude:: examples/create-winsyslog-demo-table.sql
      :language: sql

   If you prefer the command line, save the same script locally as
   ``create-winsyslog-demo-table.sql`` and run it with ``sqlcmd``:

   .. code-block:: powershell

      sqlcmd -S localhost -E -i .\create-winsyslog-demo-table.sql

   If you already use the PowerShell ``SqlServer`` module, this is the same
   step with ``Invoke-Sqlcmd``:

   .. code-block:: powershell

      Invoke-Sqlcmd -ServerInstance localhost -InputFile .\create-winsyslog-demo-table.sql

2. Create and test an ODBC **System DSN** on the WinSyslog host.

   If you want to create the DSN from PowerShell instead of the GUI, run the
   helper script below in an elevated PowerShell session on the WinSyslog
   host. It creates a System DSN named ``WinSyslogDemo`` and can be adjusted
   for a different server or driver if needed.

   .. literalinclude:: examples/create-winsyslog-demo-dsn.ps1
      :language: powershell

   After the script finishes, open **Data Sources (ODBC)** and test the new
   System DSN before you continue.

   You can also run this small PowerShell connection test against the DSN:

   .. code-block:: powershell

      $connection = [System.Data.Odbc.OdbcConnection]::new('DSN=WinSyslogDemo;')
      $connection.Open()
      $connection.Close()
      Write-Host 'DSN connection test succeeded.'

   If you prefer the GUI instead, use these steps:

   - Open **Data Sources (ODBC)** on the WinSyslog host.
   - Create a new **System DSN** for SQL Server and name it
     ``WinSyslogDemo``.
   - Select the Microsoft SQL Server driver that matches your environment, for
     example Microsoft ODBC Driver 18 for SQL Server.
   - Point the DSN to the SQL Server instance and database created in the
     previous step.
   - Complete the DSN wizard and use its built-in connection test.

3. Create or choose the WinSyslog ruleset whose messages should be stored.

   - If you are starting from scratch, use the ruleset that receives your
     incoming syslog traffic.
   - If you already have a working ruleset, reuse it.

4. Add a :doc:`Write to Database <../mwagentspecific/a-databaseoptions>`
   action to that ruleset.

5. Configure the database action.

   - Select the ODBC **System DSN** ``WinSyslogDemo``.
   - Enter the database credentials if the DSN or driver requires them.
   - Set the table name to ``dbo.WinSyslogIncoming``.
   - Keep the SQL statement type at the normal ``INSERT`` path.
   - Leave output encoding at ``System Default`` unless you know you need a
     different one.
   - Do **not** use **Create Database** for this quick start because the table
     is created by the SQL script above.

   .. image:: ../images/a-odbcdatabase-connection.png
      :width: 100%
      :alt: Write to Database connection settings in the WinSyslog client

   *The connection tab is the main place to select the DSN, enter credentials,
   and verify the connection before you save the action.*

6. Configure the field list so it matches the demo table.

   - Remove any fields that do not belong in the demo table.
   - Use these mappings:

     - ``received_at`` -> ``DateTime`` -> ``timereported``
     - ``source_host`` -> ``varchar`` -> ``source``
     - ``facility_text`` -> ``varchar`` -> ``syslogfacility_text``
     - ``severity_text`` -> ``varchar`` -> ``syslogpriority_text``
     - ``app_name`` -> ``varchar`` -> ``syslogappname``
     - ``raw_message`` -> ``text`` -> ``rawsyslogmsg``
     - ``message_text`` -> ``text`` -> ``msgPropertyDescribed``

   .. image:: ../images/a-odbcdatabase-datafields.png
      :width: 100%
      :alt: Database field mapping grid in the WinSyslog client

   *The datafields tab is where you turn one incoming syslog event into the
   structured columns shown in the example table.*

7. Save and apply the configuration.

   - Restart the WinSyslog service if your environment or workflow requires it.

8. Send a test message.

   - For the fastest first verification, use **Tools -> Send Syslog Test
     Message**.
   - To reproduce the sample row above, send an RFC 5424 syslog message with
     the same values from any syslog client.

9. Verify the inserted rows in SQL Server.

   - Open SSMS and query the demo table.
   - Confirm that the row contains the expected values.

   .. code-block:: sql

      SELECT TOP (10) *
      FROM dbo.WinSyslogIncoming;

   If you prefer the command line, run the same check with ``sqlcmd``:

   .. code-block:: powershell

      sqlcmd -S localhost -E -Q "SELECT TOP (10) * FROM dbo.WinSyslogIncoming;"

Verification
------------

1. The ODBC **System DSN** test succeeds.
2. The WinSyslog action connects successfully to the DSN.
3. A test message produces a new row in ``dbo.WinSyslogIncoming``.
4. The row contains both the raw syslog line and the structured message
   columns.

Common issues
-------------

- The DSN was created as a user DSN instead of a **System DSN**. See
  :doc:`FAQ: Why Does My WinSyslog Database Setup Fail? <faq/database-logging-troubleshooting>`.
- The DSN points to the wrong SQL Server instance or database. See
  :doc:`FAQ: Why Does My WinSyslog Database Setup Fail? <faq/database-logging-troubleshooting>`.
- The SQL Server account can connect but does not have permission to create
  rows. See
  :doc:`FAQ: Why Does My WinSyslog Database Setup Fail? <faq/database-logging-troubleshooting>`.
- The table name in WinSyslog does not match the SQL table name exactly. See
  :doc:`FAQ: Why Does My WinSyslog Database Setup Fail? <faq/database-logging-troubleshooting>`.
- The field list still contains the default schema rows instead of the demo
  table columns. See
  :doc:`FAQ: Why Does My WinSyslog Database Setup Fail? <faq/database-logging-troubleshooting>`.
- The message sender is not reaching the same ruleset that holds the database
  action. See
  :doc:`FAQ: Why Does My WinSyslog Database Setup Fail? <faq/database-logging-troubleshooting>`.
- The data type in the table is too short for the message text and truncation
  occurs. See
  :doc:`tutorial-custom-database-integration`.

Next step
---------

If this quick start works and you want to adapt the schema to your own
application, continue with:

- :doc:`tutorial-custom-database-integration`

See also
--------

- :doc:`../mwagentspecific/a-databaseoptions`
- :doc:`faq/database-logging-troubleshooting`
- :doc:`producttour/store-and-forward`
- :doc:`faq/database-formats`
