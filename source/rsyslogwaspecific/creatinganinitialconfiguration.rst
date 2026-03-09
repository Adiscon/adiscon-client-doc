.. _rsyslogwa-initial-configuration:

Creating an Initial Configuration
=================================

Use this page to build the first working rsyslog Windows Agent configuration:
collect Windows Event Log events and forward them to an rsyslog receiver.

Goal
----

At the end of this procedure, rsyslog Windows Agent will:

- monitor one or more Windows event logs
- process matching events through a ruleset
- forward them to a remote rsyslog server

Prerequisites
-------------

- rsyslog Windows Agent is installed.
- You can open the rsyslog Windows Agent Configuration Client.
- The rsyslog Windows Agent service is installed on the system.
- You know the destination host, port, and transport mode expected by the
  receiver.

Steps
-----

1. Create a ruleset.

   - In the rsyslog Windows Agent Configuration Client, create a new ruleset.
   - Leave filtering simple for the first test so that visible events can
     match.

2. Add one forwarding action to that ruleset.

   - Inside the ruleset, add a
     :doc:`Forward Syslog <a-forwardsyslogoptions>` action.
   - Enter the receiver host and port.
   - Choose the transport mode expected by the receiver.

3. Create one event collection service.

   - Under :doc:`Services <services>`, add an
     :doc:`Event Log Monitor V2 <../mwagentspecific/eventlogmonitorv2>`
     service.
   - Bind that service to the ruleset you created.
   - Select at least one Windows event log or channel to monitor.

4. Save and apply the configuration.

   - Apply or save the changes in the Configuration Client so the service can
     use them.
   - Until you apply the changes, the running service continues to use the
     previous configuration.

5. Start or restart the rsyslog Windows Agent service if required.

How to verify
-------------

1. Trigger or wait for a Windows event that should be visible.
2. Confirm that the receiver gets the forwarded event.
3. If nothing arrives, check:

   - the rsyslog Windows Agent service is running
   - the event collection service is enabled
   - the service is bound to the correct ruleset
   - the forwarding action is inside that ruleset
   - the receiver host, port, and transport mode are correct

Expected result
---------------

If the configuration is correct, rsyslog Windows Agent reads Windows Event Log
data and forwards matching events to the configured receiver.

Next step
---------

- To refine matching behavior, continue with :doc:`process-and-filter`.
- To learn about forwarding options, continue with :doc:`store-and-forward`.
