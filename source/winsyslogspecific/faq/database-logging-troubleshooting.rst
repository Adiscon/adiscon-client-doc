.. _winsyslog-database-logging-troubleshooting:

Why Does My WinSyslog Database Setup Fail?
===========================================

Question
--------

Why does my first WinSyslog database logging setup fail to write rows into SQL
Server or another ODBC database?

Answer
------

The most common causes are:

- the DSN was created as a user DSN instead of a **System DSN**
- the ODBC driver does not match the WinSyslog service architecture
- the DSN works for the interactive user but not for WinSyslog running under
  its default ``Local System`` service account
- the SQL account can connect but cannot insert into the target table
- the table name in WinSyslog does not match the real table name
- the field list still reflects the default schema instead of the custom table
- the rule or service that should receive the test message is not active

Details
-------

For a first setup, WinSyslog database logging usually fails for one of three
reasons:

1. The database connection itself is wrong.
2. The action points at the wrong table or column mapping.
3. The test message never reaches the ruleset that contains the database
   action.

Use the following checks in order.

Quick checks
^^^^^^^^^^^^

1. Test the ODBC DSN outside WinSyslog first.

   - Open **Data Sources (ODBC)**.
   - Confirm that the DSN is a **System DSN**.
   - Confirm that the driver connects to the intended SQL Server instance and
     database.
   - If the DSN uses Windows authentication, remember that WinSyslog normally
     runs under the default Windows ``Local System`` service account unless you
     changed it.
   - A DSN test that succeeds for the interactive admin user does not prove
     that the WinSyslog service can connect with the same DSN and database
     access.

2. Test the WinSyslog action connection.

   - Open the **Write to Database** action.
   - Click **Verify Database**.
   - If the verify step fails, fix the DSN or credentials before testing
     anything else.

3. Confirm the target table name.

   - If you use a custom table, the table name in WinSyslog must match the
     actual SQL table exactly.
   - If you use the default Adiscon schema, keep the built-in table names.

4. Confirm the field list.

   - A custom table must use a field list that matches the table columns.
   - Remove default-schema rows that do not belong to the custom table.

5. Confirm that the message reaches the ruleset.

   - Make sure the input service is enabled.
   - Make sure the service is bound to the ruleset that contains the database
     action.
   - Make sure the message you test actually matches the rule conditions.

Common failure patterns
^^^^^^^^^^^^^^^^^^^^^^^

- **DSN works in Windows but not in WinSyslog**

  This usually means the service cannot see the same DSN definition or the
  DSN was created for the wrong account scope. Recreate it as a **System DSN**.

- **Verify Database succeeds, but no rows appear**

  This usually means the table name, field list, or ruleset binding is wrong.
  Recheck the action settings and confirm that the incoming message actually
  triggers the rule.

- **The DSN test works for the admin user, but WinSyslog still cannot write**

  This usually means the DSN or SQL permissions were only validated for the
  interactive user account. WinSyslog normally runs under the default Windows
  ``Local System`` service account unless you changed it, so a remote SQL
  Server may see a different account than your admin session.

  Recheck the authentication mode and either grant SQL access to the WinSyslog
  service account context, change the WinSyslog service to run under an
  account that already has SQL access, or use SQL authentication instead.

- **Rows appear, but values are missing or truncated**

  This usually means the destination column is too short or the wrong WinSyslog
  property is mapped. Widen the SQL column or use a shorter property replacer
  expression.

- **SQL Server rejects the insert**

  This usually means the database account lacks insert permission or the table
  schema does not match the action's field list. Check both permissions and the
  column definitions.

- **The setup works until the database is unavailable**

  This usually means you should enable the database action's queue settings so
  WinSyslog can buffer writes while the database is offline.

Action path
-----------

1. Verify the DSN in Windows ODBC administration.
2. Use **Verify Database** in the WinSyslog action.
3. Confirm the table name and field list.
4. Confirm that the message reaches the correct ruleset.
5. Send the test message again and query the target table in SQL Server.

Related information
-------------------

* :doc:`../tutorial-database-logging`
* :doc:`../tutorial-custom-database-integration`
* :doc:`../../mwagentspecific/a-databaseoptions`
* :doc:`database-formats`
* :doc:`queue-buildup-sql-server-cleanup`
