Include Event ID in Syslog message while forwarding to a Syslog server
======================================================================

We are using MonitorWare Agent / EventReporter to forward
`Windows Event logs to a Syslog server <https://www.adiscon.com/step-by-step-guide/forwarding-nt-event-logs-to-syslog-server/>`_ .
The resulting syslog message does not have the Event IDs in them. How can we
make Event ID part of the actual Syslog message?

One of the proposed solution would be to `forward the Event Log messages using
SETP Server <https://www.adiscon.com/step-by-step-guide/forwarding-nt-event-logs-to-an-setp-server/>`_ . The resulting message would have the Event IDs in them.
`Click here <https://www.adiscon.com/faq/difference-setp-and-syslog/>`_ to know the difference between SETP and Syslog!

But there are other ways to include the Event ID even without using
:doc:`setp <../glossaryofterms/setp>` (which is obviously not an option if you
would like to send to a non-Adiscon backend).

So you can do one of the following:

**Use XML Format** - This is the best recommended option. With XML format, you get

everything about this event and you get it in a well-structured way. It
includes all of the properties described in our
:doc:`event properties reference <../shared/references/eventspecificproperties>`.
To enable XML format, simply check "Use XML to Report" in the
:doc:`forward syslog options <../mwagentspecific/a-forwardsyslogoptions>` Action.
Use Custom Format - In the "Forward Syslog" action, you can specify your own
custom format in the "Message Format" text box. By default it is set to %msg%,
but you can include whatever you like. Use the "Insert" link to do this (or
simply type it)! Be sure to read the
:doc:`property replacer <../shared/references/eventproperties>` documentation to see
the full power. This option is a good one, especially if you intend to parse
the data because *you* can exactly specify what you would like to see.
Use MoniLog Format - This is our former legacy format. It includes a bunch of
useful information, but it has a number of anomalies, which might hit you in
few cases when parsing. We do not recommend it, but if you would like to use
it, you can select the "Insert" link in the "Forward Syslog" action properties.
Then, select "Replace with MoniLog Format". It will generate a custom format of
the type given below. Again, we do not recommend this, but it is a way.
``## %severity% %timereported:::uxTimeStamp%: %source%/%sourceproc% (%id%) - "%msg%" ##.``

**Change Event Log Monitor Settings** - You could also change the Event Log Monitor

itself to generate the legacy format. Then, you do not need to change the
"Forward Syslog" action's settings. The big drawback is that now the Event Log
Monitor does emit an old format, which is not meant to be processed by any
other MonitorWare product. If you just use the product as a back-end for your
own front-end, this is not an issue. Anyhow, we still recommend to go for
approach #3 instead of this. If you absolutely want to do it this way, this is
how it is done:
Go to the :doc:`event log monitor properties <../mwagentspecific/eventlogmonitorv1>`.
Click on the "Advanced Options" button. Check the "Use Legacy Format" checkbox.
This will enable some other checkboxes. Review the options to see which of
these you want.

We have provided the options at hand. We *strongly* recommend to go for either
option 1 or 2. If you choose option 3 or 4, you can receive a parsing error
from time to time. However this has been solved after introducing the newer
formats.

As a general hint, you may want to take into account that Windows Event Log
messages can become rather lengthy. They often go over the syslog RFC size of
1024 bytes. If you run a non-Adiscon Syslog server, you need to ensure it can
receive such large messages, because otherwise some information might be
missing (with option 2, you can customize what you would like to be missing in
such cases - by limiting the size of %msg% via the property replacer).
