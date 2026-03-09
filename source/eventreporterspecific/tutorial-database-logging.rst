.. _eventreporter-tutorial-database-logging:

Tutorial: Write Windows Events to a Database
============================================

Use this tutorial when EventReporter should store matching events in an
ODBC-accessible database.

Goal
----

At the end of this procedure, EventReporter will write matching events into a
database table through an ODBC System DSN.

Prerequisites
-------------

- A reachable database server
- An ODBC **System DSN** on the EventReporter host
- Credentials with the required permissions for inserts and table creation, if
  applicable

Steps
-----

1. Prepare the database connection outside EventReporter.

   - Create an ODBC **System DSN** on the EventReporter host.
   - Verify that the database is reachable and that the credentials are valid.

2. Create or choose the ruleset whose events should be stored.
3. Add a :doc:`Write to Database <../mwagentspecific/a-databaseoptions>`
   action.
4. Configure the database action.

   - Select the System DSN.
   - Enter credentials if the DSN requires them.
   - Use the default table format unless you have a defined reason to change
     it.

5. Save and apply the configuration.
6. Restart the EventReporter service if required.
7. Trigger a matching event.

Verification
------------

1. Confirm that the database connection succeeds.
2. Query the target table and verify that the event was inserted.
3. If no row appears, check the DSN type, credentials, table settings, and
   database permissions.

Next step
---------

If the basic insert path works, continue with:

- :doc:`../mwagentspecific/a-databaseoptions`
- :doc:`faq/database-formats`
