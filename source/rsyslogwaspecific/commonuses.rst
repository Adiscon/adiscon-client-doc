Common Uses
===========

Rsyslog Windows Client can be used in several ways, due to its set of features.

The most common use is to forward Windows EventLogs to a central Syslog server,
which is usually Rsyslog. That means, the EventLog will be polled for new
entries and they will be forwarded to Rsyslog via syslog. Basically, the
transition of Windows Events to Linux should be the most common case.

In addition to the Windows EventLog, text file-based logs are the second-most to
be forwarded. These text file logs could be from a web server like IIS or
anything else.

The third common case would be the syslog relay. This could happen if you have
several sites, but no Linux server on each site. Then you could as well use a
Windows machine to receive all the log messages, no matter if it is EventLogs,
web server logs or regular syslog. You could then filter it if necessary and
forward all logs again to a central location.
