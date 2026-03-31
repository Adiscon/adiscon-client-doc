.. _mwagent-tutorial-custom-database-integration:

Tutorial: Integrate MonitorWare Agent with a Custom Database Schema
===================================================================

Use this tutorial when MonitorWare Agent should write into an existing database
schema instead of the built-in ``SystemEvents`` layout.

Goal
----

At the end of this procedure, MonitorWare Agent will write matching events or
messages into your own destination table.

When to choose this tutorial
----------------------------

Use this path when:

- your organization already has a fixed database schema
- another application expects specific column names or data types
- you want MonitorWare Agent to feed an existing integration or reporting
  database

Do not use this path just because database logging exists. If you want the
fastest supported setup or Adiscon-compatible default tables, use
:doc:`tutorial-database-logging` instead.

What this tutorial does not do
------------------------------

This tutorial does not design your schema for you. MonitorWare Agent can write
to your table, but you must decide the table design, column definitions,
indexes, retention strategy, and downstream reporting logic.

Prerequisites
-------------

- A reachable target database
- A working ODBC or OLE DB connection path appropriate for the chosen database
  action
- A destination table that already exists
- Database credentials with permission to insert rows into that table
- A clear mapping from MonitorWare Agent properties to the destination columns

Example target table
--------------------

The exact schema is up to you. For a SQL-based example, a custom table could
look like this:

.. code-block:: sql

   CREATE TABLE IncomingMonitorWareData (
       recorded_at datetime NOT NULL,
       source_host varchar(255) NOT NULL,
       info_unit_type int NOT NULL,
       message_text text NOT NULL
   );

Steps
-----

1. Review the destination schema before opening MonitorWare Agent.

   - Confirm the exact table name.
   - Confirm each destination column name and data type.
   - Decide which MonitorWare Agent property belongs in each column.

2. Create and test the database connection outside MonitorWare Agent.

   - For ODBC, create and test an ODBC **System DSN**.
   - For OLE DB, configure and test the provider path required by your target
     database.

3. Create or choose the ruleset whose events or messages should be stored.

4. Add the database action that matches your connection path.

   - Use :doc:`ODBC Database Options <a-databaseoptions>` for ODBC.
   - Use :doc:`OLEDB Database Action <a-oledbdatabaseaction>` for OLE DB.

5. Configure the connection settings and use **Verify Database** to confirm
   connectivity.

6. Point the action to the existing destination table.

   - Enter the custom table name.
   - Do **not** use **Create Database** for this path unless you intentionally
     want the built-in default schema instead of your own table.

7. Replace the default field list with mappings that match your schema.

   For the example table above, a practical starting point is:

   - ``recorded_at`` -> ``DateTime`` -> ``timegenerated``
   - ``source_host`` -> ``varchar`` -> ``source``
   - ``info_unit_type`` -> ``int`` -> ``iut``
   - ``message_text`` -> ``text`` -> ``msg``

   Depending on the data source, you can add more specific columns. For example,
   Windows Event Log data often benefits from an ``id`` column, while syslog
   data may benefit from ``syslogpriority`` or ``syslogtag``.

   If a string column is shorter than the source property, use the property
   replacer to truncate or transform the value deliberately. For example,
   ``%msg:1:200%`` stores only the first 200 characters of the message.

8. Save and apply the configuration.

9. Restart the service if required in your environment.

10. Trigger matching data and query the destination table to verify the inserted
    rows.

Verification
------------

1. The database connection test succeeds.
2. Matching data inserts rows into the existing custom table.
3. Each value appears in the expected destination column with the expected data
   type and length.

Common issues
-------------

- Leaving the default field list unchanged while targeting a custom table
- Using the wrong field type for a destination column
- Forgetting that long text may not fit into a short ``varchar`` column
- Clicking **Create Database** even though the goal is an existing custom schema
- Assuming Adiscon tools that expect the default schema will continue to work
  unchanged against the custom table

Next step
---------

If the custom integration path works, continue with:

- :doc:`a-databaseoptions`
- :doc:`a-oledbdatabaseaction`
- :doc:`faq/database-formats`

If you later decide that you need the built-in Adiscon table layout instead of
your own schema, switch to :doc:`tutorial-database-logging`.
