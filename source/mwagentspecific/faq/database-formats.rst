.. _mwagent-database-formats-faq:

Which Database Format Should I Use with MonitorWare Agent?
==========================================================

Question
--------

Which database format should I use with MonitorWare Agent, and what should I
consider before logging events or messages into a database?

Answer
------

Use the default MonitorWare Agent database format when you want the fastest
supported setup or compatibility with the standard Adiscon table layout. Use a
custom schema when MonitorWare Agent must integrate with an existing database
design.

MonitorWare Agent is not limited to an "internal schema" path. Its database
actions can write to supported databases with user-defined schemas, as long as
you configure the table name and field mapping correctly.

For most production deployments, use a server-grade database such as Microsoft
SQL Server, MySQL, MariaDB, or PostgreSQL. Avoid Microsoft Access for
production logging.

Details
-------

MonitorWare Agent can write events or messages into a database through
:doc:`ODBC Database Options <../a-databaseoptions>` or
:doc:`OLEDB Database Action <../a-oledbdatabaseaction>`.

The built-in default format is the safest choice for first-time setup because
it matches the fields that Adiscon tools expect and avoids unnecessary mapping
work. However, the database actions are also general integration features: they
can write to your own table and column layout when that is the real
requirement.

Use the default format when:

* you are setting up database logging for the first time
* you want predictable field mapping
* you plan to use the built-in **Create Database** flow
* you plan to analyze the data with Adiscon-compatible or standard SQL tooling
* you do not have an existing schema that MonitorWare Agent must integrate with

Use a custom format only when:

* your organization already has a fixed schema
* another system requires specific column names or data types
* you have tested the mapping and understand the compatibility impact

What the database action does not do
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The database actions are writers and mapping layers. They do not design your
schema, choose your indexes, or build your reporting model for you. If you
choose a custom schema, you own the destination database design.

Action path
-----------

1. Decide whether you need the default supported schema or integration with an
   existing custom schema.
2. Decide whether your environment should use the ODBC or OLE DB path.
3. Create and test the matching database connection.
4. In MonitorWare Agent, add the matching database action to the ruleset that
   should store data.
5. For the default schema path, follow :doc:`../tutorial-database-logging`.
6. For the custom integration path, follow
   :doc:`../tutorial-custom-database-integration`.
7. Trigger matching data and verify that a row is inserted into the intended
   table.

Related information
-------------------

* :doc:`../a-databaseoptions`
* :doc:`../a-oledbdatabaseaction`
* :doc:`../tutorial-database-logging`
* :doc:`../tutorial-custom-database-integration`
* :doc:`mariadb-odbc-support <../../shared/faq/mariadb-odbc-support>`
