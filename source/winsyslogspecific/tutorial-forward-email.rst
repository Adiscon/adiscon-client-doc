.. _winsyslog-tutorial-forward-email:

Tutorial: Send Matching Messages by Email
=========================================

Use this tutorial when WinSyslog should send selected messages to an email
recipient.

Goal
----

At the end of this procedure, WinSyslog will send matching events as email
messages through a configured SMTP server.

Prerequisites
-------------

- A reachable SMTP server
- A sender address accepted by that server
- At least one target recipient address

Steps
-----

1. Create or choose the ruleset that should trigger email alerts.
2. Add a :doc:`Send Email <../mwagentspecific/a-mailoptions>` action.
3. Configure the SMTP connection.

   - Enter the mail server name or IP address.
   - Set the SMTP port.
   - Enable authentication if your server requires it.
   - Enable TLS or SSL only if the mail server supports it.

4. Configure sender and recipient fields.
5. Keep the first test simple.

   - Start with one recipient and a broad but temporary matching rule.

6. Save the configuration and restart the WinSyslog service if required.

Verification
------------

1. Trigger a matching event or send a controlled test message.
2. Confirm that the email reaches the recipient mailbox.
3. If it does not arrive, verify SMTP connectivity, authentication, and any
   mail relay restrictions.

Next step
---------

If the basic alert works, narrow the matching rule and review:

- :doc:`../mwagentspecific/a-mailoptions`
- :doc:`producttour/store-and-forward`
