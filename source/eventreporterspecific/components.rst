.. index:: Components

Components
==========

EventReporter Client
--------------------

The EventReporter Client is used to configure all components and features of
EventReporter. The client can also be used to create a configuration profile on
a base system. That profile can later be distributed to a large number of
target systems.

EventReporter Service
---------------------

The EventReporter Service - called "the service" - runs as an Windows Service and
coordinates all log processing and forwarding activity at the monitored system
(server or workstation).

The service is the only component that needs to be installed on a monitored
system. The EventReporter service is called the product "engine". As such, we
call systems with only the service installed the :doc:`engine-only <../shared/gettingstarted/informationforamassrollout>` installations.

The EventReporter service runs in the background without any user intervention.
It can be controlled via the control panel "services" applet or the "Computer
Management" MMC. The service operates as follows:

After starting, it periodically reads the Windows Event Log. Each message is
formatted and then sent to the given Syslog daemon or email recipient. After
all entries have been read, EventReporter goes to sleep and waits a given
amount of time without any processing. This so-called "sleep period" is user
configurable. As soon as the service returns from the sleep period, it once
again iterates through the Windows event logs. This processing continues until
the process is stopped.

Due to its optimized structure, EventReporter uses only very minimal processing
power. How much it uses mainly depends on how long the sleep period is. We
recommend a sleep period between 1 and 5 minutes for Syslog delivery and some
hours up to 1 day for email delivery. However, feel free to customize this
value according to your needs. We strongly recommend not using sleep periods of
500 milliseconds or less (although possible).

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
