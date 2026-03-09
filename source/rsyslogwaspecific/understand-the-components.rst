.. _rsyslogwa-tour-understand-components:

Understand the Components
=========================

rsyslog Windows Agent is easiest to understand if you separate its main
components by role.

The two main components
-----------------------

1. **rsyslog Windows Agent Service**
   This is the runtime component. It runs in the background as a Windows
   service, collects events, evaluates rules, and forwards matching data.
2. **rsyslog Windows Agent Configuration Client**
   This is the administrative user interface. You use it to define services,
   rulesets, filters, and actions. Changes are made in the Configuration
   Client and then applied so the running service can use the new
   configuration.

How they fit together
---------------------

- The **service** performs the actual collection, filtering, and forwarding
  work.
- The **configuration client** defines what the service should do.
- The service continues using the currently applied configuration until you
  save or apply changes from the client.

Optional downstream tools
-------------------------

rsyslog Windows Agent commonly forwards events to a central rsyslog server. In
some environments, stored data may later be reviewed with tools such as
Adiscon LogAnalyzer, but those are downstream systems, not core product
components.

What to read next
-----------------

- To understand the main event path, continue with
  :doc:`collect-and-forward-windows-events`.
- To build a first working setup, continue with
  :doc:`creatinganinitialconfiguration`.
- To understand rule processing, see :doc:`process-and-filter`.
