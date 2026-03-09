.. _eventreporter-tutorial-write-to-file:

Tutorial: Collect Windows Events and Write Them to a File
=========================================================

Use this tutorial when EventReporter should collect Windows Event Log data and
store matching events in a local text file.

Goal
----

At the end of this procedure, EventReporter will:

- monitor one or more Windows event logs
- pass matching events through a ruleset
- write them to a file on disk

Prerequisites
-------------

- A writable target directory for log files
- At least one ruleset for incoming events
- An Event Log Monitor service that will bind to that ruleset

Steps
-----

1. Create or choose a ruleset.
2. Add a **Write to File** action.

   - Inside that ruleset, add a
     :doc:`Write to File <../mwagentspecific/a-fileoptions>` action.

3. Configure the target file.

   - Set **File Path Name** to the directory where EventReporter should write
     the files.
   - Set **File Base Name** to the logical file name prefix.
   - Keep the default extension unless you need something specific.

4. Create or choose an Event Log Monitor service.

   - Use :doc:`Event Log Monitor V2 <../mwagentspecific/eventlogmonitorv2>` for
     new setups unless you have a compatibility reason to use V1.
   - Bind the service to the ruleset that contains the file action.

5. Save and apply the configuration.
6. Start or restart the EventReporter service if required.

Verification
------------

1. Trigger or wait for a Windows event that should match.
2. Open the configured directory.
3. Confirm that EventReporter created or updated the expected log file.

Next step
---------

If file logging works, continue with:

- :doc:`creating-an-initial-configuration`
- :doc:`../mwagentspecific/a-fileoptions`
- :doc:`store-and-forward`
