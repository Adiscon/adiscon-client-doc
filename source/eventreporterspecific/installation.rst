.. index:: Installation

Installation
============

Use this page to install EventReporter and prepare the system for initial
configuration.

Before you begin
----------------

Make sure that:

- the target system runs a supported version of Windows
- you have local administrative rights for the installation
- the system can install required Microsoft .NET components if they are not yet
  present
- you know whether this system will run the full product or only the background
  service in a deployment scenario

Supported platforms
-------------------

Current EventReporter releases are intended for modern Windows versions,
including Windows 10, Windows 11, Windows Server 2016, Windows Server 2019,
Windows Server 2022, Windows Server 2025, and newer compatible releases.

For detailed platform notes, see :doc:`systemrequirements`.

Installation steps
------------------

1. Download the current EventReporter installer from the
   `EventReporter download page <https://www.eventreporter.com/download/>`_.
2. Run the installer with administrative rights.
3. Select the components you want to install.

   - The **EventReporter Service** is the runtime component.
   - The **EventReporter Configuration Client** is the administrative UI.

4. Finish the installer.
5. Start the EventReporter Configuration Client.
6. Create or review the initial configuration.
7. Apply the configuration so the EventReporter service uses the current
   settings.

What gets installed
-------------------

A standard installation includes:

- the EventReporter service
- the EventReporter Configuration Client
- supporting program files and libraries
- local help content shipped with the product

What to do next
---------------

After installation, continue with:

- :doc:`understand-the-components`
- :doc:`collect-windows-events`
- :doc:`creating-an-initial-configuration`
