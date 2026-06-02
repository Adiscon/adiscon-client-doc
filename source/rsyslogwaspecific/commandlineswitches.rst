.. index:: Command Line Switches

Command Line Switches
=====================

There are several command line switches available for using rsyslog Windows
Agent from the command line. To use these switches you need administrative
rights.

- ``-h`` Show command line help
- ``-v`` Show version information and whether the service is installed
- ``-i`` Install service
- ``-u`` Remove (uninstall) service
- ``-i <CustomServiceName>`` Install service with a custom service name
- ``-u <CustomServiceName>`` Uninstall a service with a custom service name
- ``-r`` Run as console application
- ``-r -o`` Run once as console application

If you install the service, you can start and stop it with commands such as
``net start``, ``net stop``, ``sc start``, ``sc stop``, or PowerShell
(``Start-Service`` / ``Stop-Service``). By using the ``-r`` switch, you run it
only on the command line. When you close the command line, the program will
stop working.

The ``-v`` switch gives you information about the version of the service.

**Custom service name examples:**

- ``rsyslogd.exe -i CustomServiceName``
- ``rsyslogd.exe -u CustomServiceName``

You can import Adiscon Config Format (cfg) configuration files via the
command line as well. The syntax is quite easy. Simply execute the rsyslog
Windows Agent configuration client and append the name of the configuration
file.

**Sample:**

RsyslogConfigClient.exe example.cfg

or

RsyslogConfigClient.exe "example.cfg"

After this is executed, you will see the splash screen of the configuration
client and then the import dialogue, which you have to confirm manually.

For doing a silent import, the ``/f`` parameter has to be appended. This will
look like this:

``RsyslogConfigClient.exe "example.cfg" /f``
