.. _autostart-interactive-syslog-viewer:


How to Autostart Interactive Syslog Viewer
===========================================

.. meta::
   :created: 2026-01-07
   :updated: 2026-01-07
   :products: SyslogViewer

Overview
--------

This FAQ explains how to configure Interactive Syslog Viewer to start automatically when Windows boots, ensuring continuous syslog monitoring without manual intervention.

Background
----------

Interactive Syslog Viewer is a Windows application designed for real-time syslog message monitoring and analysis. By default, it must be launched manually after each system startup. For production environments or dedicated monitoring systems, automatic startup provides continuous availability.

The application supports command-line parameters that enable auto-listening mode, making it suitable for unattended operation.

Methods for Autostarting Interactive Syslog Viewer
---------------------------------------------------

There are two primary methods to configure Interactive Syslog Viewer to start automatically on Windows:

Method 1: Using Windows Startup Folder (Recommended for Current User)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method starts the application automatically when the current user logs in.

**Steps:**

1. **Locate the Startup folder**

   - Press ``Win + R`` to open the Run dialog
   - Type ``shell:startup`` and press Enter
   - This opens the Startup folder for the current user

2. **Create a shortcut to Interactive Syslog Viewer**

   - Navigate to the Interactive Syslog Viewer installation directory (typically ``C:\Program Files (x86)\MonitorWare Agent\`` or ``C:\Program Files (x86)\WinSyslog\``)
   - Right-click on ``InterActive SyslogViewer.exe``
   - Select "Create shortcut"
   - A shortcut will be created in the same directory

3. **Configure the shortcut with command-line parameters**

   - Right-click the newly created shortcut and select "Properties"
   - In the "Target" field, add the ``/autolisten`` parameter after the executable path
   - Example: ``"C:\Program Files (x86)\MonitorWare Agent\InterActive SyslogViewer.exe" /autolisten``
   - Optionally, add other parameters such as ``/port=10514`` to customize the listening port
   - Click "OK" to save changes

4. **Move the shortcut to the Startup folder**

   - Cut the configured shortcut from the installation directory
   - Paste it into the Startup folder opened in step 1

5. **Verify the configuration**

   - Restart your computer or log off and log back in
   - Interactive Syslog Viewer should start automatically and begin listening for syslog messages

Method 2: Using Windows Task Scheduler (Recommended for System-Wide Startup)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method starts the application at system boot, regardless of user login, making it suitable for dedicated monitoring servers.

**Steps:**

1. **Open Task Scheduler**

   - Press ``Win + R`` to open the Run dialog
   - Type ``taskschd.msc`` and press Enter
   - Task Scheduler opens

2. **Create a new task**

   - In the right pane, click "Create Task..." (not "Create Basic Task")
   - This opens the Create Task dialog

3. **Configure General settings**

   - **Name:** Enter a descriptive name, such as "Interactive Syslog Viewer Autostart"
   - **Description:** Optional description, e.g., "Automatically starts Interactive Syslog Viewer at system boot"
   - **Security options:**
     
     - Select "Run whether user is logged on or not"
     - Check "Run with highest privileges" if the application requires elevated permissions
     - Choose the user account under which the task should run

   - **Configure for:** Select your Windows version from the dropdown

4. **Configure Triggers**

   - Switch to the "Triggers" tab
   - Click "New..." to create a new trigger
   - In "Begin the task:" dropdown, select "At startup"
   - Optionally, set a delay (e.g., 30 seconds) to allow other services to start first
   - Click "OK" to save the trigger

5. **Configure Actions**

   - Switch to the "Actions" tab
   - Click "New..." to create a new action
   - **Action:** Ensure "Start a program" is selected
   - **Program/script:** Enter the full path to Interactive Syslog Viewer executable
     
     Example: ``C:\Program Files (x86)\MonitorWare Agent\InterActive SyslogViewer.exe``

   - **Add arguments (optional):** Enter command-line parameters
     
     Example: ``/autolisten /port=10514``

   - Click "OK" to save the action

6. **Configure Conditions (Optional)**

   - Switch to the "Conditions" tab
   - Review power and network conditions as needed
   - For dedicated monitoring servers, consider unchecking "Start the task only if the computer is on AC power"

7. **Configure Settings**

   - Switch to the "Settings" tab
   - Recommended settings:
     
     - Check "Allow task to be run on demand"
     - Check "Run task as soon as possible after a scheduled start is missed"
     - Uncheck "Stop the task if it runs longer than" (to allow continuous operation)

   - Click "OK" to create the task

8. **Test the configuration**

   - In Task Scheduler, find your newly created task
   - Right-click the task and select "Run"
   - Verify that Interactive Syslog Viewer starts correctly
   - Restart your computer to confirm automatic startup

Available Command-Line Parameters
----------------------------------

Interactive Syslog Viewer supports the following command-line parameters for customization:

- ``/autolisten`` - Automatically start the syslog server upon launch
- ``/port=<port_number>`` - Override the configured listening port (e.g., ``/port=10514``)
- ``/windowpos <x>,<y>,<width>,<height>`` - Set the default window position and size (e.g., ``/windowpos 0,0,512,800``)
- ``/?`` - Display available command-line options

Example combined usage:

.. code-block:: text

   "C:\Program Files (x86)\MonitorWare Agent\InterActive SyslogViewer.exe" /autolisten /port=514 /windowpos 0,0,1024,768

Troubleshooting
---------------

**Issue: Application starts but doesn't listen for syslog messages**

**Solution:**

- Ensure the ``/autolisten`` parameter is included in the shortcut or Task Scheduler action
- Verify that no other application is using the configured port
- Check Windows Firewall settings to ensure the port is not blocked

**Issue: Task Scheduler task doesn't start the application**

**Solution:**

- Verify that the full path to the executable is correct in the Task Scheduler action
- Ensure the user account configured for the task has permission to run the application
- Check the Task Scheduler history for error messages (enable history in Task Scheduler if not visible)
- Verify "Run whether user is logged on or not" is selected if you want system-wide startup

**Issue: Application closes unexpectedly after startup**

**Solution:**

- Review Windows Event Viewer for application errors
- Ensure all required dependencies are installed
- Try running the application manually with the same parameters to identify issues
- Verify that the application has write access to its configuration directory

**Issue: Permission denied errors**

**Solution:**

- Run Task Scheduler as Administrator when creating the task
- Ensure "Run with highest privileges" is checked in the task's General settings
- Verify the user account has appropriate permissions for the installation directory

Additional Considerations
-------------------------

**Port Conflicts:**

By default, Interactive Syslog Viewer may use port 514 (standard syslog port). If another syslog service is running on the same system, use the ``/port=`` parameter to specify an alternative port.

**Firewall Configuration:**

Ensure Windows Firewall allows incoming connections on the configured syslog port. You may need to create an inbound rule for the port used by Interactive Syslog Viewer.

**Resource Usage:**

Interactive Syslog Viewer is designed for interactive viewing and may consume GUI resources even when running unattended. For production syslog collection, consider using WinSyslog or MonitorWare Agent instead, which are optimized for server-side operation.

**Log File Growth:**

If collecting high-volume syslog data, monitor disk space and configure appropriate log rotation or retention policies.

Best Practices
--------------

1. **Use Task Scheduler for production systems** - Provides better control and logging of startup events
2. **Set appropriate delays** - Add a 30-60 second delay in Task Scheduler to allow network and other services to initialize
3. **Test thoroughly** - Always test the autostart configuration by restarting the system
4. **Document the configuration** - Keep records of command-line parameters and task settings for future reference
5. **Monitor system resources** - Ensure the system has adequate resources for continuous syslog viewing
6. **Consider alternatives for production** - For production syslog collection without GUI requirements, use WinSyslog or MonitorWare Agent

Summary
-------

Interactive Syslog Viewer can be configured to start automatically on Windows using either the Startup folder (for user-based startup) or Task Scheduler (for system-wide startup). The ``/autolisten`` command-line parameter enables automatic syslog listening, making the application suitable for unattended monitoring scenarios.

For production environments requiring robust syslog collection, logging, and processing capabilities, consider using WinSyslog or MonitorWare Agent, which are designed specifically for server-side syslog operations.
