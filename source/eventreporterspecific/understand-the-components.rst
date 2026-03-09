.. _eventreporter-tour-understand-components:

Understand the Components
=========================

EventReporter is easiest to understand if you separate its main components by
role.

The two main components
-----------------------

1. **EventReporter Service**
   This is the runtime component. It runs in the background as a Windows
   service, reads Windows Event Log data, evaluates rules, and then stores or
   forwards matching events.
2. **EventReporter Configuration Client**
   This is the administrative user interface. You use it to define services,
   rulesets, filters, and actions. Changes are made in the Configuration
   Client and then applied so the running EventReporter service can use the new
   configuration.

How they fit together
---------------------

- The **service** performs the actual collection, filtering, storage, and
  forwarding work.
- The **configuration client** defines what the service should do.
- The service continues using the currently applied configuration until you save
  or apply changes from the client.

What to read next
-----------------

- To understand where EventReporter gets data, start with
  :doc:`collect-windows-events`.
- To build a first working setup, continue with
  :doc:`creating-an-initial-configuration`.
- To understand rule processing, see :doc:`process-and-filter`.
