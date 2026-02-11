.. _mass-rollout-deployment-winsyslog:


How to Perform a Mass Rollout of WinSyslog
===========================================

.. meta::
   :author: Adiscon GmbH
   :created: 2026-02-11
   :updated: 2026-02-11
   :products: WinSyslog

Overview
--------

This FAQ explains how to efficiently deploy WinSyslog to multiple machines using automated mass rollout techniques. This approach is ideal for organizations deploying WinSyslog across multiple systems with identical or similar configurations.

When to Use Mass Rollout
-------------------------

A mass rollout is appropriate when:

* Deploying to 5 or more machines
* Automating distribution across multiple systems
* Setting up remote offices with identical configurations
* Standardizing syslog infrastructure across an organization

**Note:** For fewer than 5 systems, manual installation may be more economical unless configurations are very complex.

Approach Overview
-----------------

The mass rollout process involves:

1. Creating a master configuration on one system
2. Exporting the configuration to a registry file
3. Distributing the registry file and service executable to target systems
4. Importing the configuration and starting the service

Step-by-Step Automated Rollout
-------------------------------

Step 1: Create Master Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Install WinSyslog on a master system
2. Configure all rules, services, and actions as desired
3. Test the configuration thoroughly
4. Export the configuration using the Configuration Client

Step 2: Export Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open the WinSyslog Configuration Client
2. Go to "Computer" menu
3. Select "Export Settings to Registry File"
4. Specify a filename (e.g., ``winsyslog-config.reg``)
5. Save the file

Step 3: Prepare for Distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to distribute:

* **Service executable:** ``winsyslg.exe`` (from installation directory)
* **Helper DLLs:** Required DLL files
* **Configuration file:** The exported ``.reg`` file

Step 4: Automated Installation Script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a batch file to automate the installation::

    @echo off
    REM Mass Rollout Script for WinSyslog
    REM This script installs and configures WinSyslog on target machines

    REM Copy service executable from network share
    copy \\servershare\winsyslg.exe c:\winsyslog\
    copy \\servershare\*.dll c:\winsyslog\

    REM Navigate to installation directory
    cd c:\winsyslog

    REM Register the service (creates registry entries)
    winsyslg.exe -i

    REM Import the configuration
    regedit /s \\servershare\winsyslog-config.reg

    REM Start the service
    net start "AdisconWINSyslog"

    echo WinSyslog installed and started successfully

Engine-Only Installation
------------------------

For locked-down environments or when you don't want to run the full setup program:

* **No Windows RPC required:** Engine-only install doesn't require incoming RPC connections
* **Minimal footprint:** Only essential service files needed
* **Direct execution:** Files can be copied and service registered directly

**Important:** The ``winsyslg.exe -i`` command does NOT copy files. It assumes they are already in their final location and only creates the necessary registry entries to register WinSyslog as a Windows service.

Branch Office Deployment
-------------------------

For remote offices where some manual intervention is acceptable:

Preparation (Central Office)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Complete installation on one machine
2. Configure settings as desired
3. Export configuration to ``.reg`` file
4. Copy the following files to a CD or network share:

   * ``winsyslg.exe``
   * ``winsyslg.pem``
   * Required DLL files
   * Configuration ``.reg`` file

Installation (Branch Office)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create installation directory (e.g., ``C:\Program Files\WinSyslog``)
2. Copy all files from CD to the directory
3. Run ``winsyslg.exe -i`` from that directory
4. Double-click the ``.reg`` file to import configuration
5. Start the service using Services Manager or ``net start "AdisconWINSyslog"``

Modern Deployment Alternatives
-------------------------------

For contemporary environments, consider these options:

* **Group Policy:** Use GPO to deploy registry files and execute installation scripts
* **PowerShell DSC:** Desired State Configuration for automated deployment
* **Configuration Management:** Integrate with SCCM, Ansible, or similar tools
* **Cloud Deployment:** Automate via cloud-init scripts for virtual machines

Best Practices
--------------

* **Test first:** Always test deployment on a non-production system
* **Document changes:** Keep track of configuration modifications
* **Backup existing:** Backup any existing configuration before deployment
* **Verify service:** Check that service starts correctly after deployment
* **Monitor logs:** Review event logs for any installation issues
* **Update paths:** Ensure file paths are appropriate for target environment

Troubleshooting
---------------

Common issues and solutions:

**Service won't start**
    Verify executable permissions and file paths

**Configuration not applied**
    Check registry import was successful

**Missing DLLs**
    Ensure all required DLL files are copied

**Port conflicts**
    Verify syslog ports aren't already in use

**Firewall issues**
    Ensure Windows Firewall rules are configured

Additional Notes
----------------

* The installation directory becomes the permanent program directory – do not delete it
* All configuration is stored in the Windows registry
* Service name is ``AdisconWINSyslog`` (internal name)
* Consider using file-based configuration (``.cfg`` files) for Server Core deployments
* For high-availability, plan for service dependencies and startup order

See Also
--------

* :doc:`../installation` - WinSyslog installation documentation
* :doc:`../configuringwinsyslog` - Configuration guide
* :doc:`../generaloptions` - General options reference
