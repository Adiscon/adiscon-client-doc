.. highlight:: rst
.. index:: Add-on Components

Add-on Components
=================

Adiscon offers several optional components as free downloads.

All optional components seamlessly integrate with the MonitorWare common
database format.

database format.
----------------

InterActive SyslogViewer
------------------------

The `InterActive SyslogViewer
<https://www.adiscon.com/tools/adiscons-interactive-SyslogViewer/>`_
is a Windows GUI application that receives and displays Syslog events.
It functions as a standalone Syslog server. Typically, you use it
in conjunction with a Syslog Forward Rule within the service, but it
can also operate independently.

Although not a core component, the MonitorWare Agent installation
set includes it.

For more information, see the `InterActive SyslogViewer online manual
<https://www.adiscon.com/files/pdf/SyslogViewer.pdf>`_.

Adiscon LogAnalyzer
-------------------

`Adiscon LogAnalyzer <https://loganalyzer.adiscon.com>`_ provides a
convenient web-based interface to access events gathered by MonitorWare.
It supports all major browsers.

Adiscon LogAnalyzer offers an easy-to-use solution for Browse Syslog
messages, Windows Event Log data, and other network events via the web.
It enables system administrators to quickly and easily review their
central log repository. It provides commonly used views for log data
and integrates with web resources for simple analysis of data found
in the logs.

Its primary benefit is offering a quick overview of current system
activity and allowing access to log data even when you cannot access
the administrator workstation (e.g., when traveling or moving through
the enterprise). While initially designed to work with Adiscon's
MonitorWare product line, you can easily modify it to integrate
with other solutions.

Adiscon LogAnalyzer is included in the MonitorWare Agent installation
set; the installer copies it to the machine but does not automatically
install it. For installation instructions, refer to the documentation
in the Adiscon LogAnalyzer's ``doc`` folder or see the `online manual
<https://loganalyzer.adiscon.com/doc/>`_.

Tools Available from the Tools Folder
-------------------------------------

Logger
------

Adiscon **Logger** is a command-line tool for Windows that functions like the UNIX ``logger`` command. This re-written tool offers enhanced
functionality while supporting all popular UNIX options. It also
provides reliable syslog transport via :rfc:`3195` and plain TCP, a
feature found in other Adiscon products and tools like syslog-ng.
Additionally, Logger includes options specifically for the Windows
environment.

For more details, visit: `An UNIX-like logger for Windows
<https://www.adiscon.com/tools/an-unix-like-logger-for-windows/>`_.

LogZip
------

Adiscon **LogZip** is a command-line tool for Windows that zips log files. Its primary purpose is to collect log files and store them
in a specified ZIP archive. You can easily integrate LogZip with the
Windows Task Scheduler, allowing you to automatically archive and move
unneeded log files to a different location. This keeps only recent
log files available for review.

.. note::
   LogZip requires the Microsoft .NET Framework to run. Ensure you have
   it installed.



For more details, visit: `LogZip - Archiving tool for Windows
<https://www.adiscon.com/tools/logzip-archiving-tool-for-windows/>`_.

LogDeleter
----------

Adiscon **LogDeleter** is a database log deleter and backup tool for Windows.

`LogDeleter <https://www.adiscon.com/tools/logdeleter/>`_ can delete
database records older than a specified number of days and offers the
option to back up data first. It operates via an ODBC database
connection. For example, you can run it through a Scheduled Task once
a week to back up and delete old records.

LogDeleter is part of `Adiscon's MonitorWare solution
<https://www.adiscon.com/products/>`_.

LogViewer
---------

The **LogViewer** tool efficiently processes very large log files.
While other tools often struggle with files larger than 100 MB,
Adiscon's LogViewer handles files exceeding 1 GB with ease. It
performs almost as quickly with 5 GB files as it does with 5 MB files.

A special highlighting option assists in reviewing logs. You can define
rules to highlight any keyword or phrase, associating terms with
specific colors. This feature proves particularly useful when searching
for specific errors or other log entries.
