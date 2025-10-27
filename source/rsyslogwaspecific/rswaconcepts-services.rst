Rsyslog WindowsAgent - Services
===============================

Services gather events data. For example, the Syslog server service accepts
incoming Syslog messages and the Event Log Monitor extracts Windows Event Log
data. There can be unlimited multiple services. Depending on the service type,
there can also be multiple instances running, each one with different settings.

You must define at least one service, otherwise the product does not gather
event data and hence does not perform any useful work at all. Sometimes,
services are mistaken with service defaults those are pre-existing in the tree
view. Service defaults are just the templates that carry the default properties
assigned to a service, when one of the respective type is to be created. Service
defaults are NOT executed and thus cannot gather any data.


**The following services are supported:**


**Heartbeat**

This service generates a special information type. Its primary purpose is to
notify a receiving system that WinSyslog, set for heart beating is still alive.
So the receiving system can be configured to raise alarms (or corrective
actions) if it does not receive heartbeats from WinSyslog.


**MonitorWare Echo Reply**

A central agent running the Rsyslog WindowsAgent is using the echo request and
instructs to poll each of the other WinSyslog services. When the request is not
carried out successfully, an alert is generated. The MonitorWare echo protocol


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
