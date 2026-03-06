.. _cluster-server-support-mwagent:

Running MonitorWare Agent on a Windows Cluster Server
=====================================================

.. meta::
   :author: Adiscon GmbH
   :created: 2026-03-06
   :updated: 2026-03-06
   :products: MonitorWare Agent

Question
--------

Can MonitorWare Agent run on a Windows Cluster Server, and are there any particular issues to be aware of?

Answer
------

Yes. MonitorWare Agent runs on a Windows Cluster node without problems. However, MonitorWare Agent does not include built-in cluster failover support. If a node fails, you must start the MonitorWare Agent service on another node manually or through a cluster script. The steps below explain how to prepare the cluster for this scenario.

Step 1: Set the Service Startup Type
-------------------------------------

On every cluster node **except** the primary node, set the MonitorWare Agent service startup type to **Manual**:

1. Open the Windows Service Manager (Start > Control Panel > Administrative Tools > Services).
2. Locate the service named **AdisconMonitorWareAgent**.
3. Right-click the service and select **Properties**.
4. Set **Startup type** to **Manual**.
5. Click **Apply**, then **OK**.

On the primary node, leave the startup type set to **Automatic** so that MonitorWare Agent starts automatically after a reboot.

Step 2: Mirror the Configuration Between Nodes
-----------------------------------------------

MonitorWare Agent stores its configuration in the Windows registry. To replicate a working configuration from one node to another, export it as a registry file and import it on each secondary node:

1. Open the MonitorWare Agent Configuration Client on the primary node.
2. Go to the **Computer** menu.
3. Select **Export Settings to Registry File**.

   * Choose the standard registry format (do **not** select a binary format).
   * Select the correct architecture (Win32 or x64) for your system.

4. Save the ``.reg`` file to a network share or removable media.
5. On each secondary node, double-click the ``.reg`` file to import the configuration.

After importing, the secondary node has the same configuration as the primary node. When a failover is needed, start the MonitorWare Agent service on the secondary node using the Services Manager or from the command line:

.. code-block:: bat

   net start "AdisconMonitorWareAgent"

Best Practices
--------------

* **Keep configurations in sync.** After every configuration change on the primary node, re-export and re-import the registry file on all secondary nodes.
* **Test failover regularly.** Verify that the MonitorWare Agent service starts correctly and processes messages on each secondary node.
* **Use automation.** Consider a cluster resource script or a scheduled task that starts the MonitorWare Agent service on a secondary node when the primary node becomes unavailable.
* **Verify firewall rules.** Ensure that the necessary network ports are open on all cluster nodes so that monitoring and log forwarding continue to work after failover.
