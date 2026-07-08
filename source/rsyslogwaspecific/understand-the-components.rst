.. _rsyslogwa-tour-understand-components:

Understand the Components
=========================

rsyslog Windows Agent is easiest to understand if you separate its main
components by role.

The two main components
-----------------------

1. **rsyslog Windows Agent Service**
   This is the runtime component. It runs in the background as a Windows
   service, runs the configured input services, evaluates rules, and forwards
   matching data.
2. **rsyslog Windows Agent Configuration Client**
   This is the administrative tool. You use it to define input
   services, rulesets, filters, and actions. Changes are made in the
   Configuration Client and then applied so the running service can use the new
   configuration.

How they fit together
---------------------

- The **rsyslog Windows Agent service** performs the actual collection,
  filtering, and forwarding work through the configured input services.
- The **configuration client** defines what those input services, rulesets,
  and actions should do.
- The runtime service continues using the currently applied configuration until
  you save or apply changes from the client.

For the current split between remote administration and browser-based review,
see :doc:`../shared/faq/remote-administration-and-browser-based-review`.

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
