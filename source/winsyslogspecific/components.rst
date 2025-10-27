.. index:: Components

Components
==========

WinSyslog Configuration Client
------------------------------

The WinSyslog Configuration Client - called "the Client" - is used to configure
all components and features of the WinSyslog Service. The Client can also be
used to create a configuration profile on a base system. That profile can later
be distributed to a large number of target systems.

WinSyslog Service
-----------------

The WinSyslog Service - called "the service" runs as an Windows Service and
coordinates all log processing and forwarding activity at the monitored system
(server or workstation).

The service is the only component that needs to be installed on a monitored
system. The WinSyslog service is called the product "engine". As such, we
call systems with only the service installed the :doc:`engine-only <../shared/gettingstarted/informationforamassrollout>` installations.

The service runs in the background without any user intervention. It can be
controlled via the control panel "services" applet or the "Computer Management"
MMC. The Client can also be used to control service
instances

x64 Build
---------

The installer inherits the 32bit as well as the 64bit edition. It determines
directly, which version is suitable for your operating system and therefore
installs the appropriate version. Major compatibility changes for the x64
platform have been made in the Service core. For details see the changes listed
below:

* ODBC Database Action fully runs on x64 now. Please note that there are
  currently very few ODBC drivers for x64 available!

* Configuration Registry Access, a DWORD Value will now be saved as QWORD into
  the registry. However the Configuration Client and Win32 Service Build can
  handle these data type and convert these values automatically into DWORD if
  needed. The Configuration Client will remain a win32 application. Only the
  Service has been ported to the x64 platform.

A note on cross updates from Win32 to x64 Edition of EventReporter!
-------------------------------------------------------------------

It is not possible to update directly from Win32 to x64 Edition using setup
upgrade method. The problem is that a minor upgrade will NOT install all the
needed x64 components. Only a full install will be able to do this. Therefore,
in order to perform a cross update, follow these instructions:

1. Create a backup of your configuration, save it as registry or xml file (See
   the Configuration Client Computer Menu)

2. Uninstall EventReporter.

3. Install EventReporter by using the x64 Edition of the setup.

4. Import your old settings from the registry or xml file.
