.. _rsyslogwa-configuring:

Configure rsyslog Windows Agent
===============================

Use this page to understand how the rsyslog Windows Agent Configuration Client
is organized and how changes reach the running service.

How configuration works
-----------------------

The rsyslog Windows Agent service runs in the background once it is installed
and configured. The Configuration Client is the administrative UI used to define
services, rulesets, filters, and actions.

Changes are made in the Configuration Client and then applied so the running
service can use the new configuration. Until you apply the changes, the service
continues using the previous active configuration.

How the tree is organized
-------------------------

The tree view has three main areas:

- **General / Defaults** for product-wide settings and default templates
- **Running Services** for active inputs such as Event Log Monitor, File
  Monitor, or Syslog Server
- **RuleSets** for the processing logic that evaluates filters and actions

Defaults vs. active instances
-----------------------------

Default objects are templates. They provide pre-filled values for new services
or actions, but they do not collect, process, or forward anything by
themselves. Actual work only happens in the active service and action
instances you create under **Running Services** and the selected rulesets.

How data moves through the product
----------------------------------

1. A configured **service** collects an event.
2. That service sends the event into its assigned **ruleset**.
3. Each **rule** evaluates its filter conditions in order.
4. Matching **actions** forward, enrich, route, or discard the event.

Common editing tasks
--------------------

- To add an input, right-click **Running Services** and create the service you
  need.
- To add processing logic, create or edit a ruleset under **RuleSets**.
- To change output behavior, edit the actions inside the relevant rule.
- To enable new settings for the service, save or apply the configuration after
  editing.

What to read next
-----------------

- :doc:`core-concepts`
- :doc:`services`
- :doc:`filterconditions`
- :doc:`actions`
