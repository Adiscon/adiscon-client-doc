.. _mwagent-initial-configuration:

Creating an Initial Configuration
=================================

Goal
----

Create a first working MonitorWare Agent configuration that collects Windows
Event Log records and writes matching events to a local file.

In this manual, **input** is the plain-language concept, while the configured
object is a **service**.

Prerequisites
-------------

- MonitorWare Agent is installed.
- The **MonitorWare Agent Configuration Client** starts successfully.
- You have local administrative rights on the system.

Steps
-----

1. Open the MonitorWare Agent Configuration Client.
2. Under **Running Services**, add an
   :doc:`Event Log Monitor V2 <eventlogmonitorv2>` service.
3. Assign that input service to a new ruleset, for example `Initial Windows Events`.
4. In the ruleset, create one rule.
5. Leave the filter condition broad for the first test, or add one simple
   filter such as an event source or event ID condition.
6. Add a :doc:`Write to File <a-fileoptions>` action to the rule.
7. Configure a local test path and filename.
8. Save and apply the configuration in the Configuration Client so the running
   input service uses the new settings.
9. Restart the MonitorWare Agent service if your environment or change-control
   process requires it.

How to verify
-------------

1. Trigger an event that should match the Event Log Monitor service and rule.
2. Confirm that the configured output file is created or updated.
3. If no output appears, check:

   - whether the input service is enabled
   - whether the ruleset is assigned to that service
   - whether the filter condition is too restrictive
   - whether the output path is writable by the service account

Expected result
---------------

MonitorWare Agent collects matching Windows events and writes them to the local
file you configured.

Next step
---------

Continue with:

- :doc:`process-and-filter`
- :doc:`store-and-forward`
