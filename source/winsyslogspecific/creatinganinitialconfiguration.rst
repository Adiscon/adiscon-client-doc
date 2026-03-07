.. _winsyslog-initial-configuration:

Creating an Initial Configuration
=================================

Use this page to build the first working WinSyslog configuration: receive a
test syslog message and write it to a local file.

Goal
----

At the end of this procedure, WinSyslog will:

- listen for incoming syslog messages
- process them through a ruleset
- write them to a local file

Prerequisites
-------------

- WinSyslog is installed.
- You can open the WinSyslog Configuration Client.
- The WinSyslog service is installed on the system.

Steps
-----

1. Create a ruleset.

   - In the WinSyslog Configuration Client, create a new ruleset.
   - Leave filtering simple for the first test so that all incoming messages
     can match.

2. Add one file action to that ruleset.

   - Inside the ruleset, add a :doc:`Write to File <../mwagentspecific/a-fileoptions>` action.
   - Choose an easy-to-find test file path.

3. Create one syslog listener service.

   - Under :doc:`Services <services>`, add a
     :doc:`Syslog server service <../mwagentspecific/syslogserver>`.
   - Bind that service to the ruleset you created.
   - Keep the default listener settings unless you already know you need a
     different port or protocol.

4. Save the configuration.

   - Apply or save the changes in the Configuration Client so the service can
     use them.
   - Until you apply the changes, the running service continues to use the
     previous configuration.

5. Start or restart the WinSyslog service if required.

   - Ensure the WinSyslog service is running with the new configuration.

How to verify
-------------

1. In the WinSyslog Configuration Client, use
   ``Tools -> Send Syslog Test Message``
   (see :ref:`Send Syslog Test Message <winsyslog-send-test-message>`).
2. Confirm that the message is written to the file configured in the action.
3. If nothing arrives, check:

   - the syslog service is enabled
   - the service is bound to the correct ruleset
   - the file action is inside that ruleset
   - the WinSyslog service is running

Expected result
---------------

If the configuration is correct, WinSyslog receives the test message and stores
it in the configured file. At that point, you have a working end-to-end setup.

Next step
---------

- To understand message intake options, see
  :doc:`Receive Logs <producttour/receive-logs>`.
- To add filtering and more advanced processing, continue with
  :doc:`Process and Filter <producttour/process-and-filter>`.
- To add forwarding or additional storage targets, continue with
  :doc:`Store and Forward <producttour/store-and-forward>`.
