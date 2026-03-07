.. index:: Installation

Installation
============

.. include:: ../shared/partials/installation-overview.rst

.. only:: winsyslog

   Use this page to install WinSyslog on a Windows system and prepare it for
   initial configuration.

   Before you begin
   ----------------

   - Verify that the target system matches the supported platforms in
     :doc:`System Requirements <systemrequirements>`.
   - Decide whether you need only the WinSyslog service and configuration
     client, or also optional components such as Interactive Syslog Viewer.
   - Ensure you have local administrator rights on the target machine.

   Installation steps
   ------------------

   1. Download the current installer from the
      `Download Versions <https://www.winsyslog.com/download>`_ page.
   2. Start the setup program by double-clicking ``wnsyslog.exe``.
   3. Accept the license terms and continue through the installer wizard.
   4. Select the components you want to install.
   5. Finish the setup. The installer will add the WinSyslog program group and
      install the required runtime components if needed.

   What gets installed
   -------------------

   A standard WinSyslog installation typically includes:

   - the **WinSyslog service**, which receives and processes log data
   - the **WinSyslog Configuration Client**, which is used to configure the
     service and send test messages
   - optional UI or analysis components if you selected them during setup

   What to do next
   ---------------

   After installation, continue with
   :doc:`Understand the Components <producttour/understand-the-components>` and
   then :doc:`Creating an Initial Configuration <creatinganinitialconfiguration>`
   to build a first working setup.
