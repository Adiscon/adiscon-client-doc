
.. index:: IPv6

IPv6
====

Adiscon Products officially support IPv6. The IPv6 support was introduced with
the following versions:

* MonitorWare Agent 8.0
* WinSyslog 11.0
* EventReporter 12.0

Support for IPv6 is available in all network related facilities of the engine.
All network related actions will automatically detect IPv6 and IPv4 target
addresses if configured. You can also use DNS resolution to resolve valid IPv6
addresses. Network related Services can either use IPv4 or IPv6 as internet
protocol. In order to support both protocols, you will need to create two
services. The only exception is the RELP Listener, which uses IPv4 and IPv6
automatically if available.
