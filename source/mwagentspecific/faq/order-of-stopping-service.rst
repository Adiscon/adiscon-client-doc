.. _order-of-stopping-service-mwagent:

Recommended Service Stop Order for MonitorWare Agent Maintenance
=================================================================

.. meta::
   :author: Adiscon GmbH
   :created: 2026-03-06
   :updated: 2026-03-06
   :products: MonitorWare Agent

Question
--------

What is the recommended order for stopping the MonitorWare Agent service during system maintenance or reboots?

Answer
------

When performing system maintenance, updates, or planned reboots on a system running MonitorWare Agent, follow a specific shutdown sequence to prevent data loss and ensure a clean shutdown. The MonitorWare Agent service should be stopped **after** any web server and **before** the database server.

Recommended Stop Order
----------------------

1. **Stop IIS/Web Server** (if using a web-based log viewer)
2. **Stop MonitorWare Agent Service**
3. **Stop Database Server** (SQL Server, MySQL, etc.)

Rationale
---------

This sequence ensures:

- **Web connections are closed first:** Prevents new user sessions from accessing the database while MonitorWare Agent is still writing.
- **MonitorWare Agent stops gracefully:** Allows MonitorWare Agent to complete any in-progress writes and flush its queues before the database becomes unavailable.
- **Database closes last:** Ensures all pending transactions from MonitorWare Agent are committed before the database shuts down.

Stop Commands
-------------

You can stop the MonitorWare Agent service using its internal service name ``AdisconMonitorWareAgent`` in PowerShell or Command Prompt:

**Command Prompt:**

.. code-block:: bat

   net stop w3svc
   net stop "AdisconMonitorWareAgent"
   net stop MSSQLSERVER

**PowerShell:**

.. code-block:: powershell

   Stop-Service -Name "w3svc"
   Stop-Service -Name "AdisconMonitorWareAgent"
   Stop-Service -Name "MSSQLSERVER"

Startup Order
-------------

When starting services after maintenance, reverse the order:

1. **Start Database Server**
2. **Start MonitorWare Agent Service**
3. **Start IIS/Web Server**

**Command Prompt:**

.. code-block:: bat

   net start MSSQLSERVER
   net start "AdisconMonitorWareAgent"
   net start w3svc

**PowerShell:**

.. code-block:: powershell

   Start-Service -Name "MSSQLSERVER"
   Start-Service -Name "AdisconMonitorWareAgent"
   Start-Service -Name "w3svc"

Service Name Reference
----------------------

When managing the MonitorWare Agent service from the command line, use the internal service name:

- **Internal Service Name:** ``AdisconMonitorWareAgent``
- **Display Name:** MonitorWare Agent Service

The internal service name remains consistent across installations and should be used in automation scripts for reliability.

Verifying Service Status
------------------------

.. code-block:: powershell

   Get-Service -Name "AdisconMonitorWareAgent"

.. code-block:: bat

   sc query "AdisconMonitorWareAgent"

Best Practices
--------------

- **Plan maintenance windows:** Schedule downtime during low-traffic periods to minimize log message loss.
- **Backup database:** Perform a database backup before shutting down services.
- **Verify connections:** After restart, verify that the MonitorWare Agent service started correctly and is writing to the database.
- **Check logs:** Review the Windows Event Viewer for any MonitorWare Agent service errors after restart.
- **Use internal service names:** Always use the internal service name ``AdisconMonitorWareAgent`` in scripts for reliability.

Troubleshooting
---------------

If the MonitorWare Agent service does not stop gracefully:

- Check for stuck processes in Task Manager.
- Review the Windows Event Viewer for service errors.
- Verify that database connections are properly closed.
- Check service dependencies: ``sc qc "AdisconMonitorWareAgent"``
- As a last resort, use force stop: ``net stop "AdisconMonitorWareAgent" /y``
