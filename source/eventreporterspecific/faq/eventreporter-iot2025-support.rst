.. _eventreporter-iot2025-support:


Is EventReporter v19+ supported on Windows Server IoT 2025?
===========================================================

.. meta::
   :author: Andre Lorbach
   :created: 2025-10-07
   :updated: 2025-10-07
   :products: EventReporter

Overview
--------

This FAQ answers whether EventReporter v19+ is supported on Windows Server IoT 2025 and outlines current guidance, functional status, and considerations for deployments, including Server Core.

Notes
-----

Support Status
--------------

**Official support:**

- Windows Server IoT 2025 is not yet explicitly listed in the EventReporter v19+ platform matrix.

**Functional status:**

- EventReporter v19+ is known to function properly on Windows Server IoT 2025 (including Server Core) based on internal testing and field feedback.

Guidance for Server Core Deployments
------------------------------------

Windows Server IoT 2025 Server Core does not provide a graphical user interface. For headless deployments, we recommend configuring EventReporter using Adiscon Config Files (``*.cfg``), a portable, file-based configuration format.

Recommended workflow:

1. Create the configuration on a GUI-enabled machine
   - Install EventReporter and open the Configuration Client
   - Configure rules, services, and actions as required
   - Export the configuration as Adiscon Config Files (``*.cfg``)
2. Transfer the configuration to Server Core
   - Copy the exported ``.cfg`` to the Server Core system (e.g., via PowerShell Remoting or SMB)
3. Enable File Config Mode and set paths via registry

   Registry path: ``HKEY_LOCAL_MACHINE\SOFTWARE\Adiscon\EventReporter\Settings``

   Required values:

   - ``szFileConfig`` (REG_SZ): Example ``c:\configs\eventreporter\central-server.cfg``
   - ``szDataDirectory`` (REG_SZ): Example ``c:\configs\eventreporter\``
   - ``iAccessMode`` (REG_DWORD): ``1`` (enables file config mode)

.. admonition:: Important

   When running in file config mode, ensure the service account has read access to the configuration file and write access to the data directory.

..

..

