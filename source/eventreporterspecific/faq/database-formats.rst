.. _eventreporter-database-formats-faq:

Which Database Format Should I Use with EventReporter?
======================================================

Question
--------

Which database format should I use with EventReporter, and what should I
consider before logging events into a database?

Answer
------

Use the default EventReporter database format when you want the fastest
supported setup or compatibility with the standard Adiscon table layout. Use a
custom schema when EventReporter must integrate with an existing database
design.

EventReporter is not limited to an "internal schema" path. The database action
can write to supported ODBC-accessible databases with user-defined schemas, as
long as you configure the table name and field mapping correctly.

For most production deployments, use a server-grade database such as Microsoft
SQL Server, MySQL, MariaDB, or PostgreSQL. Avoid Microsoft Access for
production logging.

Details
-------

EventReporter can write events into an ODBC-accessible database through the
:doc:`Write to Database action <../../mwagentspecific/a-databaseoptions>`.
The built-in default format is the safest choice for first-time setup because it
matches the fields that Adiscon tools expect and avoids unnecessary mapping
work. However, the action is also a general integration feature: it can write
to your own table and column layout when that is the real requirement.

Use the default format when:

* you are setting up database logging for the first time
* you want predictable field mapping
* you plan to use the built-in **Create Database** flow
* you plan to analyze the data with Adiscon-compatible or standard SQL tooling
* you do not have an existing schema that EventReporter must integrate with

Use a custom format only when:

* your organization already has a fixed schema
* another system requires specific column names or data types
* you have tested the mapping and understand the compatibility impact

What the database action does not do
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The action is a writer and mapping layer. It does not design your schema,
choose your indexes, or build your reporting model for you. If you choose a
custom schema, you own the destination database design.

Action path
-----------

1. Decide whether you need the default supported schema or integration with an
   existing custom schema.
2. Create and test an ODBC **System DSN** on the EventReporter host.
3. In EventReporter, add a :doc:`Write to Database action <../../mwagentspecific/a-databaseoptions>`
   to the ruleset that should store events.
4. For the default schema path, follow :doc:`../tutorial-database-logging`.
5. For the custom integration path, follow
   :doc:`../tutorial-custom-database-integration`.
6. Trigger a test event and verify that a row is inserted into the intended
   table.

Related information
-------------------

* :doc:`../../mwagentspecific/a-databaseoptions`
* :doc:`../tutorial-database-logging`
* :doc:`../tutorial-custom-database-integration`
* :doc:`mariadb-odbc-support <../../shared/faq/mariadb-odbc-support>`
