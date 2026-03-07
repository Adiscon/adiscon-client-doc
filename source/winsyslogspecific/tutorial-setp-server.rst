.. _winsyslog-tutorial-setp-server:

Tutorial: Configure a SETP Server Service
=========================================

Use this tutorial when another Adiscon product should forward events to
WinSyslog via SETP.

Goal
----

At the end of this procedure, WinSyslog will listen for incoming SETP traffic
and pass received events into a ruleset.

Prerequisites
-------------

- A sending Adiscon product that supports SETP
- A ruleset with at least one visible action, such as file logging
- Port and TLS settings agreed between sender and receiver

Steps
-----

1. Create or choose a ruleset for incoming SETP events.
2. Add at least one action to that ruleset so received events are visible.

   - For a first test, a :doc:`Write to File <../mwagentspecific/a-fileoptions>`
     action is the simplest choice.

3. Add a :doc:`SETP Server <../mwagentspecific/setpserver>` service.
4. Configure the listener settings.

   - Keep the default port unless your environment requires a different one.
   - Bind to a specific IP address only if you need that behavior.
   - Enable TLS only if the sending side is configured for TLS as well.

5. Bind the service to the ruleset.
6. Save the configuration and restart the WinSyslog service if required.
7. Configure the sending system to forward to this WinSyslog instance over
   SETP.

Verification
------------

1. Send one or more events from the configured sender.
2. Confirm that the events reach the ruleset on the WinSyslog side.
3. If you used a temporary file action, verify that the events appear in the
   file.

Next step
---------

If the receiver works, continue with:

- :doc:`../mwagentspecific/setpserver`
- :doc:`producttour/receive-logs`
- :doc:`faq/setp-vs-syslog`
