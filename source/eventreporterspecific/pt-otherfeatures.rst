Other Miscellaneous Features
============================

Ease of use
-----------

Using the new EventReporter client interface, the product is very easy to setup
and customize. We also support full documentation and support for large-scale
unattended installations.

Comprehensive Windows Event Log Support
---------------------------------------

EventReporter provides complete support for all Windows Event Log formats and
systems, including modern Windows event logging infrastructure. All event log
information can be gathered, fully decoded, and submitted to log targets. This
includes support for custom event logs and advanced event log features.
EventReporter handles whatever Windows Event Log requirements you may have.

Runs on large variety of Windows Systems
----------------------------------------

This includes Windows 10, Windows 11, and Windows Server 2016/2019/2022. Workstation
or Server, 32 or 64 bits – EventReporter runs on all of them. Note: For legacy
systems (Windows XP, NT, Server 2003), older versions are available - contact
Adiscon for details.
available on request). Please note that the current builds do no longer support
older platforms, but we have previous releases available for those that need
them (the current software can no longer run on e.g. NT 3.5 platforms, because
there are technical issues mostly with the installer).

Robustness
----------

EventReporter is running in a large number of installations. It is written to
perform robustly even under unusual circumstances. Its reliability has been
proven at customers' sites since 1997.

Remote Administration
---------------------

The client can be used to remotely manage EventReporter instances.

Minimal Resource Usage
----------------------

EventReporter has no noticeable impact on system resources. It was specifically
written with minimal resource usage in mind. In typical scenarios, it's
footprint is barely traceable. This ensures it can also be installed on heavily
loaded servers.

Full Windows Event Log Decoding
-------------------------------

EventReporter can fully decode all types of Windows Event Log entries. It has
the same capabilities like event viewer.

Windows Service
---------------

The log forwarding process "the engine" is implemented as a native
multithreaded Windows service. It can be controlled via the control panel
services applet, the computer management console and any other means for
controlling services.

Double Byte Character Set Support (e. g. Japanese)
--------------------------------------------------

EventReporter supports characters encoded in double byte character sets (DBCS).
This is mostly used with Asian languages like Japanese or Chinese. All DBCS
strings are forwarded correctly to the syslog daemon or email recipient.
However, the receiving side must also be able to process DBCS correctly.
Adiscon's syslog daemon for Windows, WinSyslog, does so. The output character
encoding is selectable and support Shift-JIS, JIS and EUC-JP for Japanese users.
