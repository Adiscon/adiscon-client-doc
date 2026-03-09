.. _eventreporter-initial-configuration:

Creating an Initial Configuration
=================================

Use this page to build the first working EventReporter configuration: collect
Windows Event Log events and write them to a local file.

Goal
----

At the end of this procedure, EventReporter will:

- monitor one or more Windows event logs
- process matching events through a ruleset
- write them to a local file

Prerequisites
-------------

- EventReporter is installed.
- You can open the EventReporter Configuration Client.
- The EventReporter service is installed on the system.

Steps
-----

1. Create a ruleset.

   - In the EventReporter Configuration Client, create a new ruleset.
   - Leave filtering simple for the first test so that visible events can
     match.

2. Add one file action to that ruleset.

   - Inside the ruleset, add a :doc:`Write to File <../mwagentspecific/a-fileoptions>` action.
   - Choose an easy-to-find test file path.

3. Create one event log monitor service.

   - Under :doc:`Services <services>`, add an
     :doc:`Event Log Monitor V2 <../mwagentspecific/eventlogmonitorv2>` service.
   - Bind that service to the ruleset you created.
   - Select at least one Windows event log or channel to monitor.

4. Save and apply the configuration.

   - Apply or save the changes in the Configuration Client so the service can
     use them.
   - Until you apply the changes, the running service continues to use the
     previous configuration.

5. Start or restart the EventReporter service if required.

How to verify
-------------

1. Trigger or wait for a Windows event that should be visible.
2. Confirm that the event is written to the configured file.
3. If nothing arrives, check:

   - the EventReporter service is running
   - the event log monitor service is enabled
   - the service is bound to the correct ruleset
   - the file action is inside that ruleset
   - the selected event log or channel actually produces events

Expected result
---------------

If the configuration is correct, EventReporter reads Windows Event Log data and
writes matching events to the configured file.

Next step
---------

- To refine matching behavior, continue with :doc:`process-and-filter`.
- To forward events elsewhere, continue with :doc:`store-and-forward`.
