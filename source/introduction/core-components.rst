
.. _core-components:

Core Components
===============

.. rubric:: MonitorWare Agent Configuration Client

The *MonitorWare Agent Configuration Client* (the client)
configures all *MonitorWare Agent* components and features.
You can also use the client to create a configuration profile
on a base system. Later, you can distribute that profile to
numerous target systems.

.. rubric:: MonitorWare Agent Service

The *MonitorWare Agent Service* (the service) runs as a
Windows service and performs the actual work.

The service is the only component you need to install on a
monitored system. We call the MonitorWare Agent service the
product's "engine". Consequently, we refer to systems with
only the service installed as :doc:`engine-only <../shared/gettingstarted/informationforamassrollout>` installations.

The service operates in the background without user intervention.
You can control it via the Control Panel's "Services" applet or
the "Computer Management" MMC. Additionally,
the client allows you to control service instances.

.. rubric:: x64 Build

The installer includes both the 32-bit and 64-bit editions.
It automatically determines the appropriate version for your
operating system and installs it. We made significant
compatibility changes for the x64 platform within the Service
core. Refer to the listed changes below for details:

* **ODBC Database Action** now fully runs on x64. However, note
  that currently fewer ODBC drivers are available for x64 than
  for x32.
* **Configuration Registry Access**: The system saves a DWORD value
  as a QWORD into the registry. Both the Configuration Client and
  Win32 Service Build can handle this data type and automatically
  convert these values to DWORD if necessary. The Configuration
  Client remains a Win32 application; only we have ported the
  Service to the x64 platform.
