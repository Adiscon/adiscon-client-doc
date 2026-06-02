Tutorial: Store Data in the Default Database Schema
===================================================

Goal
----

Store events or messages from MonitorWare Agent in the built-in default
database schema.

Why this tutorial uses the default schema
-----------------------------------------

This is the fastest supported path for a first production deployment. It keeps
the built-in field mapping, works with the **Create Database** button, and is
the safest choice if you later want Adiscon-compatible tooling or predictable
support behavior.

Prerequisites
-------------

- A reachable target database
- A configured ODBC or OLE DB path appropriate for the chosen database action
- A ruleset that receives events from a MonitorWare Agent service

Steps
-----

1. Create and test the database connection outside MonitorWare Agent.

   - For ODBC, create and test an ODBC **System DSN**.
   - For OLE DB, configure and test the provider path required by your target
     database.

2. Create or choose the ruleset whose events or messages should be stored.

3. Add the database action that matches your connection path.

   - Use :doc:`ODBC Database Options <a-databaseoptions>` for ODBC.
   - Use :doc:`OLEDB Database Action <a-oledbdatabaseaction>` for OLE DB.

4. Configure the database action.

   - Select the tested connection path.
   - Keep the default table name ``SystemEvents``.
   - Keep the default field list unless you intentionally need a custom schema.

5. Use **Verify Database** to test the action configuration.

6. If the connection test succeeds, use **Create Database** to create the
   default tables.

7. Save and apply the configuration.

8. Restart the service if required in your environment.

9. Trigger matching data and confirm that rows are written.

Verification
------------

1. The database connection test succeeds.
2. The **Create Database** button creates the default tables.
3. Matching events or messages produce rows in ``SystemEvents``.

Common issues
-------------

- Using a user DSN instead of a **System DSN** for the ODBC path
- Changing the table name or field list even though the goal is the default
  supported schema
- Selecting the wrong action type for the available driver path
- Another tutorial path is actually needed because the destination must be an
  existing custom table

Next step
---------

If the default schema path works and you want to keep it, continue with:

- :doc:`a-databaseoptions`
- :doc:`tutorial-custom-database-integration`
- :doc:`store-and-forward`
- :doc:`faq/database-formats`
