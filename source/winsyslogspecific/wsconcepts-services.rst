WinSyslog - Services
====================

Services inside the WinSyslog gather the data that is processed by rules. Each
service type reflects a specific set of code inside WinSyslog. For example, a
Syslog Service represents an instance of a Syslog server and an NT Event Log
Monitor Service represents an instance of an NT Log Monitor (periodically
pulling out log information).

Typically, there can be multiple instances of the same service running, as long
as their configuration parameters do not conflict. For example the syslog
service: there can be multiple syslog servers on a given system as long as they
listen to different ports. Consequently, there can be multiple instances of the
syslog service be created. For example, there could be three of them: two
listen to the default port of 514, but one with TCP and one with UDP, and a
third one listens to UDP, port 10514. All three coexist and run at the same
time.


**The following services are supported:**


**Heartbeat**

This service generates a special information type. Its primary purpose is to
notify a receiving system that WinSyslog, set for heart beating is still alive.
So the receiving system can be configured to raise alarms (or corrective
actions) if it does not receive heartbeats from WinSyslog.


**MonitorWare Echo Reply**

A central agent running the MonitorWare Agent is using the echo request and
instructs to poll each of the other WinSyslog services. When the request is not
carried out successfully, an alert is generated. The MonitorWare echo protocol


**RELP Listener**

The RELP listener supports the new reliable event logging protocol (RELP),
which enables a more reliable transmission of messages than plain tcp syslog
protocol. The service permits to accept messages from senders who themselves
support RELP. The RELP Listener will automatically listen on all available IP
Addresses which includes IPv4 and IPv6. This is due the librelp implementation
method.

Apart from the fact that a different communication protocol is used, the RELP
listener corresponds functionally to the syslog listener. The RELP listener
automatically monitors all available IP addresses, including IPv4 and IPv6.
This is due to the Librelp implementation method.


**SETP server**

Implements an SETP Server. It is used for reliable receiving event
notifications.


**SNMP Trap Receiver**

SNMP Trap Receiver allows you to receive SNMP messages. A rough description of
a Trap is that it is somewhat like a Syslog message, just over another protocol
(SNMP). A trap is generated when the device feels it should do so and it
contains the information that the device feels should be transmitted. It also
contains some (few) standard items, as the version, community etc.


**Syslog server**

Implements a Syslog server. It can be set to listen to any valid port. UDP and
TCP communication is supported.

**Event Log Monitor**

Monitors Windows event logs. As soon as new events are detected,
these are forwarded to MonitorWare processing. This service is similar to
the Adiscon EventReporter functionality.


**Associated rulesets**

Each instance of a service has an associated ruleset. This allows easy
creation of customized rulesets on a per service basis. Of course, all
services can also operate on a common ruleset.

All services are executed as multiple threads inside the MonitorWare Agent.
From the operating point of view, there is only one system service called the
"MonitorWare Agent". If the service configuration of the MonitorWare Agent is
modified, the MonitorWare system service needs to be restarted in order to
activate the new configuration. Later releases will have some options to
automate this task.
