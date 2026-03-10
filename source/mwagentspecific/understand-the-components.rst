.. _mwagent-understand-components:

Understand the Components
=========================

MonitorWare Agent is easiest to understand when you separate its runtime,
configuration, live-viewing, and stored-data analysis roles.

MonitorWare Agent Service
-------------------------

The **MonitorWare Agent Service** is the core runtime component. It runs in the
background and performs the actual work:

- receives data from services such as Event Log Monitor, Syslog Server, SETP
  Server, File Monitor, and probes
- evaluates rules and filter conditions
- executes actions such as writing to file or database, forwarding via syslog
  or SETP, or sending notifications

Configuration Client
--------------------

The **MonitorWare Agent Configuration Client** is the administrative user
interface. Use it to create services, rulesets, rules, filters, and actions.

Changes made in the Configuration Client do not affect the running service
until you save and apply the configuration. In operational terms, the client is
where you prepare and update configuration, while the service is what runs it.

Interactive Syslog Viewer
-------------------------

**Interactive Syslog Viewer** is a separate live-viewing tool. It is useful
when you want to inspect incoming events interactively during setup,
troubleshooting, or demonstrations.

To see data there, create a forwarding rule that sends matching events from
MonitorWare Agent to the viewer.

Adiscon LogAnalyzer
-------------------

**Adiscon LogAnalyzer** works with stored log data, typically in files or a
supported database. Use it when you need browser-based review and analysis of
historical events instead of live event viewing.

How They Work Together
----------------------

A typical setup looks like this:

1. The Configuration Client defines services, rulesets, and actions.
2. The MonitorWare Agent Service runs that configuration in the background.
3. Events can be forwarded live to Interactive Syslog Viewer.
4. Events can be stored in files or a database for later analysis in Adiscon
   LogAnalyzer.
