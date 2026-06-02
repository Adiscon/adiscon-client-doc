.. _winsyslog-database-formats-faq:

Which Database Format Should I Use with WinSyslog?
===================================================

Question
--------

Which database format should I use with WinSyslog, and what should I consider
before logging messages into a database?

Answer
------

Use the default WinSyslog database format when you want the fastest supported
setup or compatibility with the standard Adiscon table layout. Use a custom
schema when WinSyslog must integrate with an existing database design.

If you want a hands-on Microsoft SQL Server example that you can reproduce
immediately, start with :doc:`../tutorial-database-logging`.

WinSyslog is not limited to an "internal schema" path. The database action can
write to supported ODBC-accessible databases with user-defined schemas, as long
as you configure the table name and field mapping correctly.

For most production deployments, use a server-grade database such as Microsoft
SQL Server, MySQL, MariaDB, or PostgreSQL. Avoid Microsoft Access for
production logging.

Details
-------

WinSyslog can write messages into an ODBC-accessible database through the
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
* you do not have an existing schema that WinSyslog must integrate with

Use a custom format only when:

* your organization already has a fixed schema
* another system requires specific column names or data types
* you have tested the mapping and understand the compatibility impact

What the database action does not do
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The action is a writer and mapping layer. It does not design your schema,
choose your indexes, or build your reporting model for you. If you choose a
custom schema, you own the destination database design.

Production recommendation
^^^^^^^^^^^^^^^^^^^^^^^^^

For production use, prefer a database engine designed for concurrent writes and
multi-user access. Microsoft Access is useful only for very small, temporary,
or lab-style setups. It is prone to locking conflicts and does not scale well
for continuous log ingestion.

This is especially important when multiple tools or users access the database
at the same time. File-based database engines are much more likely to produce
"file already in use" or similar locking problems.

Action path
-----------

1. Decide whether you need the default supported schema or integration with an
   existing custom schema.
2. Create and test an ODBC **System DSN** on the WinSyslog host.
3. If the DSN uses Windows authentication, remember that WinSyslog normally
   runs under the default Windows ``Local System`` service account unless you
   changed it. For a remote SQL Server, either grant SQL access to that
   service context, change the service logon account, or use SQL
   authentication.
4. In WinSyslog, add a :doc:`Write to Database action <../../mwagentspecific/a-databaseoptions>`
   to the ruleset that should store messages.
5. For the default schema path, follow :doc:`../tutorial-database-logging`.
6. For the custom integration path, follow
   :doc:`../tutorial-custom-database-integration`.
7. Send a test message and verify that a row is inserted into the intended
   table.

Related information
-------------------

* :doc:`../../mwagentspecific/a-databaseoptions`
* :doc:`../tutorial-database-logging`
* :doc:`../tutorial-custom-database-integration`
* :doc:`mariadb-odbc-support <../../shared/faq/mariadb-odbc-support>`
