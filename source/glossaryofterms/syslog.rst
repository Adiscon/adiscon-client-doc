
.. index:: Syslog

:orphan:

Syslog
======

Syslog is both a protocol and a system for logging messages in IP networks.
Originally developed for Unix systems, it has become the de facto standard for
system logging across multiple platforms. Syslog uses UDP port 514 by default
(though TCP and TLS variants exist) and follows formats defined in RFC 3164
(traditional) and RFC 5424 (structured). Messages include facility, severity,
timestamp, hostname, and message content. All Adiscon products support both
sending and receiving syslog messages.
