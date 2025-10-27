:orphan:

.. _glossary-mwconcepts-actions:
.. supporting-labels-marker

Actions
=======

Actions tell the Product (i.e. MonitorWare Agent or EventReporter or WinSyslog
or any of the combinations) what to do with a given event. With actions, you
can forward events to a mail recipient or Syslog server, store it in a file or
database or do many other things with it. There can be multiple actions for
each rule. These actions are described in the following section.

Write to File
-------------

The message is written to a plain text log file.

Write to Database
-----------------

The message will be written to the specified ODBC database. This database
format will be used by the MonitorWare Console that becomes available later.
Therefore, if you intend to use the console, we recommend adding at least one
rule that persists data to the database.

Write to EventLog
-----------------

The message will be written to the application event log. Please note that the
agent intentionally does not try to make the message look like it was generated
on the local system. This could be very confusing. Instead, it is written
inside the message part with standard values for event source and type.

Forward via Email
-----------------

The message will be forwarded via email. Please note that each message will
generate one email message. Messages are not combined to fit into a single
mail. The Send Mail Action includes a timeout feature (m_nTimeoutValue) that
provides control over message delivery timing.

Forward via Syslog
------------------

The message will be forwarded to a syslog daemon. UDP and TCP forwarding is
supported.

Forward via SETP
----------------

The message will be forwarded via the custom SETP protocol. This is typically
used in environments where data from different agents will be consolidated in a
central place. SETP allows to transfer all InformationUnits exactly as they
are. As such, the central repository can store an exact picture of the whole
network.

Net Send
--------

The message will be forwarded via the Windows "net send" functionality. Please
note that the Windows function is not very reliable and requires the user to be
logged in. As such, we recommend using "Net Send" only in combination with
other actions.

Start Program
-------------

The message will be passed to an external process. The command line is
specified in the action modifier.

Play Sound Action
-----------------

This action allows you to play a sound file.

Send to Communications Port
---------------------------

This action allows you to send a string to an attached communication device,
that is it sends a message through a Serial Port. It can send any message to a
configured Serial or Printer port.

Set Status
----------

This action allows you to create new properties of your own choice in the
incoming messages. There is an internal Status List within the product which
you can use for more complex filtering. You can set property over the Set
Status action and you can add filter for them. They are more or less helpers
for building complex rule constructions.

Set Property
------------

With the "Set Property" action, some properties of the incoming message can be
modified. This is especially useful if an administrator would like to e.g.
rename two equally named devices.

Call RuleSet
------------

This Action simply calls another RuleSet in some existing RuleSet. When this
Action is encountered, the Rule Engine leaves the normal flow and go to the
called RuleSet (which may contain many rules as well). It executes all the
rules that have been defined in that called RuleSet. After the execution of
all of them, it will return to its point from where it left the original flow.

Discard
-------

Please see the :doc:`rules <../glossaryofterms/rules>` description below for a complete discussion. Effectively,
the message will be discarded and any further processing of this information
unit be stopped as soon as a "Discard" action is found.

Post-Process Event Action
-------------------------

The post process action allows you to re-parse a message after it has been
processed e.g. Tab Delimited format. Such re-parsing is useful if you either
have a non-standard syslog format or if you would like to extract specific
properties from the message.
