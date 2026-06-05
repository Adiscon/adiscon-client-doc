.. _mwagent-tutorial-use-with-loganalyzer:

Tutorial: Prepare MonitorWare Agent Data for Adiscon LogAnalyzer
================================================================

Use this tutorial when MonitorWare Agent should write data that you want to
review later in Adiscon LogAnalyzer.

Goal
----

At the end of this procedure, MonitorWare Agent will write events or messages
into a database that LogAnalyzer can open.

Recommended path
----------------

For MonitorWare Agent, the recommended LogAnalyzer path is database-backed
storage. This avoids file-parser dependencies and is the most stable
integration path in the current manual.

LogAnalyzer is the browser-based review component for stored data. It is not
the MonitorWare Agent service administration interface. For that distinction,
see :doc:`../shared/faq/remote-administration-and-browser-based-review`.

Prerequisites
-------------

- A reachable database server
- A configured ODBC or OLE DB path appropriate for the chosen database action
- A MonitorWare Agent ruleset that receives the events or messages you want to
  review later
- A LogAnalyzer deployment that is ready to connect to the same database

Steps
-----

1. Complete :doc:`tutorial-database-logging` so MonitorWare Agent writes
   matching events or messages into the database.
2. Open :doc:`../shared/tutorials/loganalyzer-setup-and-use`.
3. Configure LogAnalyzer to use the same database as its data source.
4. Trigger one or more matching events or messages.

Verification
------------

1. Confirm that MonitorWare Agent writes rows into the target table.
2. Open the configured source in LogAnalyzer.
3. Verify that the stored data appears there.

Next step
---------

If you need to refine which data is stored before it appears in LogAnalyzer,
continue with:

- :doc:`process-and-filter`
- :doc:`tutorial-database-logging`

Complementary Tool: Retrospective
---------------------------------

If you need a simpler way to search and analyze log files directly instead of
using a web-based database setup, another available option is the third-party
log viewer `Retrospective <https://www.centeractive.com/products>`_ by
centeractive. It is suited for direct log file review without requiring a
central database setup.
