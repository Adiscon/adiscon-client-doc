.. _order-of-stopping-service-winsyslog:

Recommended Service Stop Order for WinSyslog Maintenance
=========================================================

.. meta::
   :author: Adiscon GmbH
   :created: 2026-03-06
   :updated: 2026-03-06
   :products: WinSyslog

Question
--------

What is the recommended order for stopping the WinSyslog service during system maintenance or reboots?

Answer
------

When performing system maintenance, updates, or planned reboots on a system running WinSyslog, follow a specific shutdown sequence to prevent data loss and ensure a clean shutdown. The WinSyslog service should be stopped **after** any web server and **before** the database server.

Recommended Stop Order
----------------------

1. **Stop IIS/Web Server** (if using a web-based log viewer)
2. **Stop WinSyslog Service**
3. **Stop Database Server** (SQL Server, MySQL, etc.)

Rationale
---------

This sequence ensures:

- **Web connections are closed first:** Prevents new user sessions from accessing the database while WinSyslog is still writing.
- **WinSyslog stops gracefully:** Allows WinSyslog to complete any in-progress writes and flush its queues before the database becomes unavailable.
- **Database closes last:** Ensures all pending transactions from WinSyslog are committed before the database shuts down.

Stop Commands
-------------

You can stop the WinSyslog service using its internal service name ``AdisconWINSyslog`` in PowerShell or Command Prompt:

**Command Prompt:**

.. code-block:: bat

   net stop w3svc
   net stop "AdisconWINSyslog"
   net stop MSSQLSERVER

**PowerShell:**

.. code-block:: powershell

   Stop-Service -Name "w3svc"
   Stop-Service -Name "AdisconWINSyslog"
   Stop-Service -Name "MSSQLSERVER"

Startup Order
-------------

When starting services after maintenance, reverse the order:

1. **Start Database Server**
2. **Start WinSyslog Service**
3. **Start IIS/Web Server**

**Command Prompt:**

.. code-block:: bat

   net start MSSQLSERVER
   net start "AdisconWINSyslog"
   net start w3svc

**PowerShell:**

.. code-block:: powershell

   Start-Service -Name "MSSQLSERVER"
   Start-Service -Name "AdisconWINSyslog"
   Start-Service -Name "w3svc"

Service Name Reference
----------------------

When managing the WinSyslog service from the command line, use the internal service name:

- **Internal Service Name:** ``AdisconWINSyslog``
- **Display Name:** WinSyslog Service

The internal service name remains consistent across installations and should be used in automation scripts for reliability.

Verifying Service Status
------------------------

.. code-block:: powershell

   Get-Service -Name "AdisconWINSyslog"

.. code-block:: bat

   sc query "AdisconWINSyslog"

Best Practices
--------------

- **Plan maintenance windows:** Schedule downtime during low-traffic periods to minimize log message loss.
- **Backup database:** Perform a database backup before shutting down services.
- **Verify connections:** After restart, verify that the WinSyslog service started correctly and is writing to the database.
- **Check logs:** Review the Windows Event Viewer for any WinSyslog service errors after restart.
- **Use internal service names:** Always use the internal service name ``AdisconWINSyslog`` in scripts for reliability.

Troubleshooting
---------------

If the WinSyslog service does not stop gracefully:

- Check for stuck processes in Task Manager.
- Review the Windows Event Viewer for service errors.
- Verify that database connections are properly closed.
- Check service dependencies: ``sc qc "AdisconWINSyslog"``
- As a last resort, use force stop: ``net stop "AdisconWINSyslog" /y``
