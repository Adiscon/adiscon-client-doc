.. _rsyslogwa-tour-process-and-filter:

Process and Filter
==================

rsyslog Windows Agent uses a rules engine to decide what to do with each
collected event: forward it, enrich it, route it differently, or drop it.

Where to configure
------------------

- :ref:`rsyslogwa-configuring` explains the tree view and how services,
  rulesets, rules, filters, and actions fit together.
- :doc:`Filter Conditions <filterconditions>` decide which events match a rule.
- :doc:`Actions <actions>` define what happens for matching events.

Recommended setup path
----------------------

1. Start with one collection service bound to one ruleset.
2. Add one simple forwarding action so results are easy to verify.
3. Add filter conditions to narrow down the events you care about.

   - Start with event source, event ID, severity, or log name.
   - Add message-content filters only after the basic event path works.

4. Add further actions only after the rule matches exactly what you intend.

Things that commonly trip people up
-----------------------------------

- Rule order matters: rules are evaluated top-to-bottom inside a ruleset.
- The service-to-ruleset binding decides which ruleset sees a collected event.
- Defaults are templates. They do not process anything until you create an
  actual service or action instance.

Next steps
----------

- Learn the underlying model in :doc:`core-concepts`.
- For the detailed tree structure, see :doc:`multiple-rulesets-rules-actions`.
