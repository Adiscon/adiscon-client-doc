.. _mass_rollout_guide:

How to Perform a Mass Rollout
=============================

A mass rollout refers to the automated deployment of Adiscon
products like `WinSyslog <https://www.WinSyslog.com/>`_ or
`EventReporter <https://www.EventReporter.com/>`_ or `MonitorWare Agent <https://www.mwagent.com/>`_ to a
significant number of machines (typically more than 5-10). This guide
outlines the recommended procedure for achieving an efficient and
consistent deployment.

The fundamental principle behind a mass rollout is to establish a
standardized configuration on a single "master" system, then
replicate this configuration and the product installation files
across all target machines. This greatly reduces manual effort and
ensures uniformity.

.. note::
   Before embarking on a mass rollout, it is highly recommended to
   familiarize yourself with the command-line switches available for
   the product you are deploying. These switches are crucial for
   unattended installation and configuration. Refer to the respective
   product's service manual (e.g., "The WinSyslog Service" or "The
   EventReporter Service") for detailed information.



1.  Create a Master (Baseline) System
-------------------------------------

The first step is to set up a single machine with the desired product
and configuration. This system will serve as your blueprint for all
subsequent deployments.

#.  **Perform a complete installation** of `WinSyslog <https://www.WinSyslog.com/>`_ or `EventReporter <https://www.EventReporter.com/>`_
    or `MonitorWare Agent <https://www.mwagent.com/>`_ on a designated master machine.
#. **Configure the product** exactly as you intend it to be on all target machines. This includes all rulesets, actions,
   destinations, and general settings. Ensure that the
   configuration is thoroughly tested and verified.

2.  Export the Master Configuration
-----------------------------------

Adiscon products store their complete configuration within the Windows
Registry. You can export this configuration to a :doc:`registry file <../../glossaryofterms/registry-file>` (.reg), which can then be imported onto other machines.

#. **Launch the product's client application** (e.g., WinSyslog Client, EventReporter Client) on your master system.
#. Navigate to the **"Computer" menu** (or similar, depending on the product version).
#. Select the option **"Export Settings to Registry File..."**.
#. A dialog will appear, prompting you to specify a filename for the
   exported settings. Choose a meaningful name (e.g.,
   ``WinSyslog_Config_Standard.reg``).
#. Save the :doc:`registry file <../../glossaryofterms/registry-file>`. This file now contains an exact
   snapshot of your master system's configuration.

.. warning::
   Ensure you select a non-binary format for exporting the registry
   settings, if prompted. Binary formats are for special purposes and
   cannot be easily reviewed or manipulated.


3.  Prepare the Deployment Package
----------------------------------

You will need to assemble a package containing the necessary
executable files and the exported configuration.

#. **Identify the core product executables and helper DLLs.** These
    are typically found in the installation directory of your master
    system. For `WinSyslog <https://www.WinSyslog.com/>`_, this would include
    ``winsyslg.exe`` and its associated DLLs. For
    `EventReporter <https://www.EventReporter.com/>`_, it would be ``mwagent.exe`` and its
    dependencies.

    * For an :doc:`engine-only install <../../glossaryofterms/engine-only-install>`, you primarily need the core service executable.

#.  **Copy these files** along with the exported :doc:`registry file <../../glossaryofterms/registry-file>`
    (e.g., ``WinSyslog_Config_Standard.reg``) to a central network share or a distribution medium (e.g., a shared folder, USB drive,
    or an ISO image).

4.  Automate the Rollout
------------------------

The actual rollout involves copying the prepared files to the target
machines, installing the product as a service, and importing the
configuration. This is typically achieved using a batch script or a
deployment tool.

Here's an example of a simple batch file that can be used for
unattended installation and configuration (adjust paths and filenames
as necessary):

.. code-block:: bat

   REM --- Copy product files to a local directory on the target machine ---
   xcopy "\\servershare\company_rollout\*" "C:\Program Files\company\WinSyslog\" /E /I /Y

   REM --- Navigate to the installation directory ---
   cd "C:\Program Files\company\WinSyslog\"

   REM --- Install the product as a service (e.g., WinSyslog) ---
   winsyslg -i

   REM --- Import the pre-configured settings from the registry file ---
   regedit.exe /s "\\servershare\company_rollout\WinSyslog_Config_Standard.reg"

   REM --- Start the product service ---
   net start "AdisconWinSyslog"

.. note::
   The ``-i`` switch for `winsyslg.exe` or `mwagent.exe` (for
   EventReporter) registers the product as a Windows service but does
   **not** copy files. It assumes the files are already at their final desired location. Therefore, ensuring the files are copied
   correctly before executing this command is crucial.

**Explanation of the batch file commands:**

* ``xcopy "\\servershare\company_rollout\*" "C:\Program Files\company\WinSyslog\" /E /I /Y``: This command copies all files and subdirectories from your network share (``\\servershare\company_rollout\``) to the target installation directory (``C:\Program Files\company\WinSyslog\``).
    * ``/E``: Copies directories and subdirectories, including empty ones.
    * ``/I``: Assumes destination is a directory if not specified.
    * ``/Y``: Suppresses prompting to confirm overwriting existing destination files.

* ``cd "C:\Program Files\company\WinSyslog\"``: Changes the current directory to the product's installation path.
* ``winsyslg -i`` (or ``mwagent -i`` for EventReporter): This command registers the application as a Windows service.
* ``regedit.exe /s "\\servershare\company_rollout\WinSyslog_Config_Standard.reg"``: This command silently imports the exported :doc:`registry file <../../glossaryofterms/registry-file>`, applying your pre-defined configuration. The ``/s`` switch ensures silent operation.
* ``net start "AdisconWinSyslog"`` (or the appropriate service name for
  EventReporter): This command starts the newly installed and
  configured service.

.. important::
   It is vital to stop the service before overwriting its files during
   an update. However, it is generally not necessary to uninstall the
   application for an upgrade, provided the local install directory


5.  Deployment Considerations
-----------------------------

* **Permissions:** Ensure that the user account performing the rollout
  has administrative privileges on the target machines for both
  installation and registry modification.
* **Centralized Deployment Tools:** For large-scale rollouts, consider
  using enterprise-grade deployment tools such as Microsoft Group
  Policy (GPO), Microsoft Endpoint Configuration Manager (MECM,
  formerly SCCM), Ansible, or similar solutions. These tools can
  orchestrate the file copy, command execution, and verification
  steps more robustly.
* **Updates:** When updating an existing :doc:`engine-only install <../../glossaryofterms/engine-only-install>`,
  you would typically upgrade your master installation, then
  distribute the new executable files and configuration using the same
  methods outlined above. It is not usually necessary to uninstall the
  previous version.
* **Branch Office Rollout:** If the goal is not fully automated
  deployment but to provide a standardized installation for local
  administrators in branch offices, you can distribute a
  pre-configured package (containing the executables and the `.reg`
  file) to them. They can then manually perform the file copy and run
  the installation/configuration commands, ensuring consistency with
  minimal effort.

This structured approach, leveraging the robust capabilities of our
products and standard Windows administration tools, enables highly
efficient and consistent mass deployments across your enterprise.
