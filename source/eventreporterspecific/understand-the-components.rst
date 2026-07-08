.. _eventreporter-tour-understand-components:

Understand the Components
=========================

EventReporter is easiest to understand if you separate its main components by
role.

The two main components
-----------------------

1. **EventReporter Service**
   This is the runtime component. It runs in the background as a Windows
   service, runs the configured input services, evaluates rules, and then
   stores or forwards matching events.
2. **EventReporter Configuration Client**
   This is the administrative tool. You use it to define input
   services, rulesets, filters, and actions. Changes are made in the
   Configuration Client and then applied so the running EventReporter service
   can use the new configuration.

How they fit together
---------------------

- The **EventReporter service** performs the actual collection, filtering,
  storage, and forwarding work through the configured input services.
- The **configuration client** defines what those input services, rulesets,
  and actions should do.
- The runtime service continues using the currently applied configuration until
  you save or apply changes from the client.

For the current split between remote administration and browser-based review,
see :doc:`../shared/faq/remote-administration-and-browser-based-review`.

What to read next
-----------------

- To understand where EventReporter gets data, start with
  :doc:`collect-windows-events`.
- To build a first working setup, continue with
  :doc:`creating-an-initial-configuration`.
- To understand rule processing, see :doc:`process-and-filter`.
