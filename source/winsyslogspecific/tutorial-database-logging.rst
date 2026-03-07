.. _winsyslog-tutorial-database-logging:

Tutorial: Write Messages to a Database
======================================

Use this tutorial when WinSyslog should store messages in an ODBC-accessible
database.

Goal
----

At the end of this procedure, WinSyslog will write matching messages from a
ruleset into a database table through an ODBC System DSN.

Prerequisites
-------------

- A reachable database server
- An ODBC **System DSN** on the WinSyslog host
- Credentials with the required permissions for inserts and table creation, if
  applicable

Steps
-----

1. Prepare the database connection outside WinSyslog.

   - Create an ODBC **System DSN** on the WinSyslog host.
   - Verify that the database is reachable and that the credentials are valid.

2. Create or choose the ruleset whose messages should be stored.
3. Add a :doc:`Write to Database <../mwagentspecific/a-databaseoptions>`
   action.
4. Configure the database action.

   - Select the System DSN.
   - Enter credentials if the DSN requires them.
   - Use the default table format unless you have a defined reason to change
     it.

5. Save the configuration and restart the WinSyslog service if required.
6. Send or receive a test message that matches the ruleset.

Verification
------------

1. Confirm that the database connection succeeds.
2. Query the target table and verify that the test message was inserted.
3. If no row appears, check the DSN type, credentials, table settings, and
   database permissions.

Next step
---------

If the basic insert path works, continue with:

- :doc:`../mwagentspecific/a-databaseoptions`
- :doc:`producttour/store-and-forward`
- :doc:`faq/database-formats`
