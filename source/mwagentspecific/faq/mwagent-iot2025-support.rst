.. _mwagent-iot2025-support:


Is MonitorWare Agent v15+ supported on Windows Server IoT 2025?
================================================================

.. meta::
   :author: Andre Lorbach
   :created: 2025-10-07
   :updated: 2025-10-07
   :products: MonitorWare Agent

Overview
--------

This FAQ answers whether MonitorWare Agent v15+ is supported on Windows Server IoT 2025 and outlines current guidance, functional status, and considerations for deployments, including Server Core.

Notes
-----

Support Status
--------------

**Official support:**

- Windows Server IoT 2025 is not yet explicitly listed in the MonitorWare Agent v15+ platform matrix.

**Functional status:**

- MonitorWare Agent v15+ is known to function properly on Windows Server IoT 2025 (including Server Core) based on internal testing and field feedback.

Guidance for Server Core Deployments
------------------------------------

Windows Server IoT 2025 Server Core does not provide a graphical user interface.
For configuration backup or transfer between GUI-enabled machines, use YAML
export (``.yaml``). Server Core service deployment still uses file config mode:
export a legacy Adiscon Config File (``.cfg``) and point ``szFileConfig`` to
that file.

Recommended workflow:

1. Create the configuration on a GUI-enabled machine

   - Install MonitorWare Agent and open the Configuration Client
   - Configure rules, services, and actions as required
   - Export YAML (``.yaml``) for backup or re-import on another GUI machine
   - For Server Core file config mode, export a legacy Config File (``.cfg``)

2. Transfer the configuration to Server Core

   - Copy the exported ``.cfg`` file to the Server Core system (e.g., via
     PowerShell Remoting or SMB)

3. Enable File Config Mode and set paths via registry

   Registry path: ``HKEY_LOCAL_MACHINE\SOFTWARE\Adiscon\MonitorWare Agent\Settings``

   Required values:

   - ``szFileConfig`` (REG_SZ): Example ``c:\configs\mwagent\central-server.cfg``
   - ``szDataDirectory`` (REG_SZ): Example ``c:\configs\mwagent\``
   - ``iAccessMode`` (REG_DWORD): ``1`` (enables file config mode)

.. admonition:: Important

   When running in file config mode, ensure the service account has read access to the configuration file and write access to the data directory.

..

..
