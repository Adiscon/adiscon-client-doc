Actions
=======

Actions tell the Product what to do with a given event. With actions, you
can forward events to a Syslog server, or send RELP messages to a system.
There can be multiple actions for each rule. These actions are described
in the following section.

Forward via Syslog
------------------

The message will be forwarded to a syslog daemon. UDP and TCP forwarding is
supported.

Send RELP
---------

This action is roughly equivalent to the "Syslog Forwarding" action, except
that it utilizes the new reliable event logging protocol (RELP) for message
transmission. It can only be used together with a RELP-enabled receiver but
then provides enhance reliability in the communications process.

Start Program
-------------

The message will be passed to an external process. The command line is
specified in the action modifier.

Play Sound Action
-----------------

This action allows you to play a sound file.

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
