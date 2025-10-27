.. _mass_update_rollout_guide:

How to Perform a Mass Update Rollout
====================================

A mass update rollout for Adiscon products like `WinSyslog <https://www.WinSyslog.com/>`_ or
`EventReporter <https://www.EventReporter.com/>`_ or `MonitorWare Agent <https://www.mwagent.com/>`_ typically involves replacing existing product
files with newer versions and optionally applying updated
configurations. The process is similar to an initial mass rollout but
requires additional steps to ensure services are stopped and restarted
correctly.

The fundamental principle remains establishing a "master" updated
configuration and package, then replicating it across target machines.

.. note::
   Always test the update procedure on a small group of non-critical
   systems before performing a large-scale rollout. This helps
   identify any unforeseen issues with the new version or
   configuration.



1.  Prepare the Master (Updated) System
---------------------------------------

First, update a single machine to the new product version and configure
it as desired. This system will serve as your blueprint for the update.

#.  **Perform an in-place upgrade** of `WinSyslog <https://www.WinSyslog.com/>`_ or `EventReporter <https://www.EventReporter.com/>`_
    or `MonitorWare Agent <https://www.mwagent.com/>`_
    on a designated master machine to the new
    version. Ensure the upgrade completes successfully.
#. **Adjust the product configuration** if necessary. This might involve new features, changed settings, or optimizations for the updated
   version. Ensure the configuration is thoroughly tested and verified.

2.  Export the Updated Master Configuration
-------------------------------------------

Export the updated configuration from your master system to a
:doc:`registry file <../../glossaryofterms/registry-file>`.

#. **Launch the product's client application** (e.g., WinSyslog Client, EventReporter Client) on your master system.
#. Navigate to the **"Computer" menu** (or similar, depending on the product version).
#. Select the option **"Export Settings to Registry File..."**.
#. Save the :doc:`registry file <../../glossaryofterms/registry-file>` (e.g.,
   ``WinSyslog_Updated_Config.reg``). This file now contains the
   updated configuration.

.. warning::
   Ensure you select a non-binary format for exporting the registry
   settings, if prompted. Binary formats are for special purposes and
   cannot be easily reviewed or manipulated.


3.  Prepare the Update Deployment Package
-----------------------------------------

Assemble a package containing the new executable files and the exported
updated configuration.

#. **Identify the new core product executables and helper DLLs** from your updated master system's installation directory.
#. **Copy these new files** along with the exported :doc:`registry file <../../glossaryofterms/registry-file>`
   (e.g., ``WinSyslog_Updated_Config.reg``) to a central network share or distribution medium.

4.  Automate the Update Rollout
-------------------------------

The update rollout involves stopping the existing service, copying the
new product files, importing the updated configuration, and restarting
the service. This is typically achieved using a batch script or a
deployment tool.

Here's an example of a simple batch file for an unattended update
(adjust paths, filenames, and service names as necessary):

.. code-block:: bat

   REM --- Define product variables ---
   SET ProductInstallPath="C:\Program Files\company\WinSyslog\"
   SET AdisconSharePath="\\servershare\company_update\"
   SET ConfigFileName="WinSyslog_Updated_Config.reg"
   SET ServiceName="AdisconWinSyslog"

   REM --- Stop the product service ---
   net stop %ServiceName%
   timeout /t 5 /nobreak >nul
   REM Optional: Add a check if the service stopped successfully

   REM --- Navigate to the installation directory ---
   cd %ProductInstallPath%

   REM --- Copy new product files, overwriting existing ones ---
   xcopy "%AdisconSharePath%*" "%ProductInstallPath%" /E /I /Y

   REM --- Import the updated pre-configured settings from the registry file ---
   regedit.exe /s "%AdisconSharePath%%ConfigFileName%"

   REM --- Start the product service ---
   net start %ServiceName%
   timeout /t 5 /nobreak >nul
   REM Optional: Add a check if the service started successfully

   REM --- Clean up (optional) ---
   REM del "%AdisconSharePath%%ConfigFileName%"

.. important::
   Stopping the service (``net stop``) **before** overwriting its files is crucial to prevent file in-use errors and ensure a clean update. The ``timeout`` command provides a brief pause to allow the service to fully stop.

**Explanation of the batch file commands:**

* ``SET ProductInstallPath=...``, ``SET AdisconSharePath=...``, etc.: Define variables for easy modification and readability.
* ``net stop %ServiceName%``: Stops the currently running Adiscon service (e.g., WinSyslog or EventReporter).
* ``timeout /t 5 /nobreak >nul``: Pauses the script for 5 seconds to allow the service to fully terminate before files are copied.
* ``cd %ProductInstallPath%``: Changes the current directory to the product's installation path.
* ``xcopy "%AdisconSharePath%*" "%ProductInstallPath%" /E /I /Y``: Copies all new files and subdirectories from your network share to
  the target installation directory, overwriting old ones.

  * ``/E``: Copies directories and subdirectories, including empty ones.
  * ``/I``: Assumes destination is a directory if not specified.
  * ``/Y``: Suppresses prompting to confirm overwriting existing destination files.

* ``regedit.exe /s "%AdisconSharePath%%ConfigFileName%"``: Silently
  imports the updated :doc:`registry file <../../glossaryofterms/registry-file>`, applying your
  pre-defined new configuration.
* ``net start %ServiceName%``: Starts the updated and reconfigured
  service.

5.  Deployment Considerations
-----------------------------

* **Permissions:** Ensure the account executing the script has
  administrative privileges on target machines.
* **Centralized Deployment Tools:** For large environments, integrate
    this batch script into tools like Microsoft Group Policy (GPO),
    Microsoft Endpoint Configuration Manager (MECM/SCCM), Ansible, or
    similar. These tools offer robust error handling, reporting, and
    scheduling.
* **Rollback Strategy:** Always have a rollback plan. This could involve
  keeping a copy of the old executables and the previous
  :doc:`registry file <../../glossaryofterms/registry-file>` in case issues arise with the new version.
* **Monitoring and Verification:** After the update, monitor key logs
  and service states on a sample of updated machines to confirm
  successful deployment and operation. Check the product's internal
  logs, Windows Event Logs, and verify that data is being processed
  correctly.

This methodical approach ensures a smooth and consistent update process
for your Adiscon product installations across your enterprise.
