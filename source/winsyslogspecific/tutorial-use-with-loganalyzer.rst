.. _winsyslog-tutorial-use-with-loganalyzer:

Tutorial: Prepare WinSyslog Data for Adiscon LogAnalyzer
========================================================

Use this tutorial when WinSyslog should write data that you want to review
later in Adiscon LogAnalyzer.

Goal
----

At the end of this procedure, WinSyslog will write messages into a database
that LogAnalyzer can open.

Recommended path
----------------

For WinSyslog, the recommended LogAnalyzer path is database-backed storage.
This avoids file-parser dependencies and is the most stable integration path in
the current manual.

Prerequisites
-------------

- A reachable database server
- An ODBC **System DSN** on the WinSyslog host
- WinSyslog access to the target database
- A LogAnalyzer deployment that is ready to connect to the same database

Steps
-----

1. Complete :doc:`tutorial-database-logging` so WinSyslog writes matching
   messages into the database.
2. Open :doc:`../shared/tutorials/loganalyzer-setup-and-use`.
3. Configure LogAnalyzer to use the same database as its data source.
4. Send or receive one or more matching messages.

Verification
------------

1. Confirm that WinSyslog writes rows into the target table.
2. Open the configured source in LogAnalyzer.
3. Verify that the stored messages appear there.

Next step
---------

If you need to refine which messages are stored before they appear in
LogAnalyzer, continue with:

- :doc:`producttour/process-and-filter`
- :doc:`tutorial-database-logging`
