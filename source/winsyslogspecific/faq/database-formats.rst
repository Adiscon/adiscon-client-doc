.. _winsyslog-database-formats-faq:

Which Database Format Should I Use with WinSyslog?
===================================================

Question
--------

Which database format should I use with WinSyslog, and what should I consider
before logging messages into a database?

Answer
------

Use the default WinSyslog database format unless you have a defined reason to
use a custom schema. For most production deployments, use a server-grade
ODBC-accessible database such as Microsoft SQL Server, MySQL, MariaDB, or
PostgreSQL. Avoid Microsoft Access for production logging.

Details
-------

WinSyslog can write messages into an ODBC-accessible database through the
:doc:`Write to Database action <../../mwagentspecific/a-databaseoptions>`.
The built-in default format is the safest choice because it matches the fields
that WinSyslog expects and avoids unnecessary mapping work.

Use the default format when:

* you are setting up database logging for the first time
* you want predictable field mapping
* you plan to analyze the data with standard SQL queries or downstream tools
* you do not have an existing schema that WinSyslog must integrate with

Use a custom format only when:

* your organization already has a fixed schema
* another system requires specific column names or data types
* you have tested the mapping and understand the operational impact

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

1. Create an ODBC **System DSN** on the WinSyslog host.
2. Verify that the database server is reachable and accepts the configured
   credentials.
3. In WinSyslog, add a :doc:`Write to Database action <../../mwagentspecific/a-databaseoptions>`
   to the ruleset that should store messages.
4. Select the System DSN.
5. Keep the default table format unless you have a strong reason to change it.
6. Send a test message and verify that a row is inserted.

Related information
-------------------

* :doc:`../../mwagentspecific/a-databaseoptions`
* :doc:`../tutorial-database-logging`
* :doc:`mariadb-odbc-support <../../shared/faq/mariadb-odbc-support>`
