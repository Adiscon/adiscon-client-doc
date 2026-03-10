.. _eventreporter-tutorial-use-with-loganalyzer:

Tutorial: Prepare EventReporter Data for Adiscon LogAnalyzer
============================================================

Use this tutorial when EventReporter should write data that you want to review
later in Adiscon LogAnalyzer.

Goal
----

At the end of this procedure, EventReporter will write Windows events into a
database that LogAnalyzer can open.

Recommended path
----------------

For EventReporter, the recommended LogAnalyzer path is database-backed storage.
This avoids file-parser dependencies and is the most stable integration path in
the current manual.

Prerequisites
-------------

- A reachable database server
- An ODBC **System DSN** on the EventReporter host
- EventReporter access to the target database
- A LogAnalyzer deployment that is ready to connect to the same database

Steps
-----

1. Complete :doc:`tutorial-database-logging` so EventReporter writes matching
   events into the database.
2. Open :doc:`../shared/tutorials/loganalyzer-setup-and-use`.
3. Configure LogAnalyzer to use the same database as its data source.
4. Trigger one or more matching Windows events.

Verification
------------

1. Confirm that EventReporter writes rows into the target table.
2. Open the configured source in LogAnalyzer.
3. Verify that the stored events appear there.

Next step
---------

If you need to refine which events are stored before they appear in
LogAnalyzer, continue with:

- :doc:`process-and-filter`
- :doc:`tutorial-database-logging`
