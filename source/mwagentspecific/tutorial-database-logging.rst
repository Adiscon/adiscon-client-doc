Tutorial: Store Events in a Database
====================================

Goal
----

Store events from MonitorWare Agent in a supported database.

Prerequisites
-------------

- A reachable target database
- A configured ODBC or OLE DB path appropriate for your action type
- A ruleset that receives events from a MonitorWare Agent service

Steps
-----

1. Create or choose the ruleset whose events should be stored.
2. Add a :doc:`Database logging <a-databaseoptions>` action to that ruleset.
3. Configure the connection and table settings.
4. Save and apply the configuration.
5. Restart the service if required in your environment.

Verification
------------

Trigger a matching event and confirm that rows are written to the target
database.
