:orphan:


.. _glossary-setp:
.. supporting-labels-marker

.. index:: SETP

SETP
====

SETP is the "Simple Event Transfer Protocol". SETP allows reliable delivery of
events between SETP supporting systems. EventReporter, WinSyslog, and
MonitorWare Agent support SETP. EventReporter works as SETP Client Only. As
such, it can forward events generated and gathered by them to central or
intermediary SETP servers. WinSyslog EnterPrise Edition works as SETP client
and server, only. The MonitorWare Agent can operate both as a SETP server and
client and as such also as a relay. It plays a vital role in a complex,
distributed environment.

SETP was developed for MonitorWare. It allows synchronous communication between
SETP clients and servers. With SETP, an event can be forwarded exactly as it
was on the original event generating system. For example, if a syslog message
is received on a remote system, that exact syslog message can be forwarded via
as many SETP relays as is configured. During that relaying, no information from
the original message is altered or lost.  As such, each of the relays as well
as the final SETP server will see the original source address, time stamps and
message.

Furthermore, SETP guarantees reliable delivery. It is based on TCP, so each of
the SETP peers know exactly that the communication partner can successfully
receive and process the message. SETP guarantees that new events are only
forwarded after the previous ones were successfully received and processed.
SETP also checks for on the wire errors. Due to its characteristics, SETP can
successfully be used in barely or occasionally connected environments like
radio connected systems.

The SETP design is influenced by many industry standard movements, most notably
the BEEP protocol and XML. However, SETP is optimized to have a very
lightweight footprint. As such, it can be implemented even in low powered
devices with little overhead.
