.. index:: Installation

Installation
============

Use this page to install rsyslog Windows Agent and prepare the system for
initial configuration.

Before you begin
----------------

Make sure that:

- the target system runs a supported version of Windows
- you have local administrative rights for the installation
- the system can install Microsoft .NET Framework 4.7.2 or a newer
  .NET Framework 4.x release for the Configuration Client if it is not yet
  present
- you know whether this system will run the full product or an engine-only
  deployment
- if this is an engine-only target, the Configuration Client is not required on
  that system and the .NET Framework requirement applies where the client is
  installed and used

Installation steps
------------------

1. Download the current installer from the
   `rsyslog Windows Agent download page <https://www.rsyslog.com/windows-agent/windows-agent-download/>`_.
2. Run the installer with administrative rights.
3. Select the components you want to install.

   - The **rsyslog Windows Agent service** is the runtime component.
   - The **rsyslog Windows Agent Configuration Client** is the administrative
     UI.

4. Finish the installer.
5. Start the rsyslog Windows Agent Configuration Client.
6. Create or review the initial configuration.
7. Apply the configuration so the service uses the current settings.

What gets installed
-------------------

A standard installation includes:

- the rsyslog Windows Agent service
- the rsyslog Windows Agent Configuration Client
- supporting program files and libraries
- local help content shipped with the product

What to do next
---------------

After installation, continue with:

- :doc:`understand-the-components`
- :doc:`collect-and-forward-windows-events`
- :doc:`creatinganinitialconfiguration`
