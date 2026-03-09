.. _eventreporter-tutorial-forward-setp:

Tutorial: Forward Windows Events via SETP
=========================================

Use this tutorial when EventReporter should forward selected Windows events to
another Adiscon product over SETP.

Goal
----

At the end of this procedure, EventReporter will forward matching Windows event
log entries via SETP.

Prerequisites
-------------

- A reachable SETP receiver
- The target host name or IP address
- Port and TLS settings agreed between sender and receiver

Steps
-----

1. Create or choose the ruleset whose events should be forwarded.
2. Add a :doc:`Forward via SETP <../mwagentspecific/a-forwardsetpoptions>`
   action.
3. Configure the receiver connection.

   - Enter the destination host name or IP address.
   - Set the destination port.
   - Enable TLS only if the receiver is configured for it.

4. Save and apply the configuration.
5. Restart the EventReporter service if required.

Verification
------------

1. Trigger a matching event.
2. Confirm that the SETP receiver gets the forwarded event.
3. If delivery fails, verify host, port, and TLS settings on both sides.

Next step
---------

If the basic path works, continue with:

- :doc:`../mwagentspecific/a-forwardsetpoptions`
- :doc:`store-and-forward`
