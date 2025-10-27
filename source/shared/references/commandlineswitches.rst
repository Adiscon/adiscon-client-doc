.. index:: Command Line Switches

Command Line Switches
=====================

There are several command line switches available for using the agent via the
command line. To use the agent via the command line you need administrative rights.


- h Shows command line help

- v Shows version information and whether or not the service is installed

- i Install service

- u Remove (uninstall) service

- i Install service with a custom servicename "CustomServiceName"

- u Uninstall a service with a custom servicename "CustomServiceName"

- r Run as console application

- r -o Run ONCE as console application


If you install the service, you can start and stop the service with the
"net start" and "net stop" commands. By using the "-r" switch, you run it only
on the command line. When you close the command line, the program will stop
working.

The "-v" switch gives you information about the version of the service.


You can import Adiscon Config Format (cfg) configuration files via the
command line as well. The syntax is quite easy. Simply execute the
configuration client and append the name of the configuration file.
This could look like this:


**Sample for MonitorWare Agent:**

mwclient.exe example.cfg

**Sample for EventReporter:**

CFGEvntSLog.exe example.cfg

**Sample for WinSyslog:**

WINSyslogClient.exe example.cfg


**Sample for Rsyslog Windows Agent:**

RsyslogConfigClient.exe example.cfg

or

**Sample for MonitorWare Agent:**

mwclient.exe "example.cfg"

**Sample for EventReporter:**

CFGEvntSLog.exe "example.cfg"

**Sample for WinSyslog:**

WINSyslogClient.exe "example.cfg"

**Sample for Rsyslog Windows Agent:**

RsyslogConfigClient.exe "example.cfg"


After this is executed, you will see the splash screen of the configuration
client and then the import dialogue, which you have to confirm manually.

For doing a silent import, the "/f" (without the quotes) parameter has to be
appended. This will look like this:

``mwclient.exe "example.cfg" /f``


In this case, the filename of the configuration has to be used with the quotes.
