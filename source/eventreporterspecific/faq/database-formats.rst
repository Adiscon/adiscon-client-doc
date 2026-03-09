.. _eventreporter-database-formats-faq:

Which Database Format Should I Use with EventReporter?
======================================================

Question
--------

Which database format should I use with EventReporter, and what should I
consider before logging events into a database?

Answer
------

Use the default EventReporter database format unless you have a defined reason
to use a custom schema. For most production deployments, use a server-grade
ODBC-accessible database such as Microsoft SQL Server, MySQL, MariaDB, or
PostgreSQL. Avoid Microsoft Access for production logging.

Details
-------

EventReporter can write events into an ODBC-accessible database through the
:doc:`Write to Database action <../../mwagentspecific/a-databaseoptions>`.
The built-in default format is the safest choice because it matches the fields
that EventReporter expects and avoids unnecessary mapping work.

Action path
-----------

1. Create an ODBC **System DSN** on the EventReporter host.
2. Verify that the database server is reachable and accepts the configured
   credentials.
3. In EventReporter, add a :doc:`Write to Database action <../../mwagentspecific/a-databaseoptions>`
   to the ruleset that should store events.
4. Select the System DSN.
5. Keep the default table format unless you have a strong reason to change it.
6. Trigger a test event and verify that a row is inserted.

Related information
-------------------

* :doc:`../../mwagentspecific/a-databaseoptions`
* :doc:`../tutorial-database-logging`
* :doc:`mariadb-odbc-support <../../shared/faq/mariadb-odbc-support>`
