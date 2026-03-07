.. _winsyslog-tour-process-and-filter:

Process and Filter
==================

WinSyslog uses a rules engine to decide what to do with each incoming event:
drop it, store it, forward it, or trigger notifications.

Where to configure
------------------

- :ref:`winsyslog-configuring` explains the tree view (Services, RuleSets, rules).
- :doc:`Filter conditions <../filterconditions>` decide which events match a rule.
- :doc:`Actions <../actions>` define what happens for matching events.

Recommended setup path
----------------------

1. Start with one input under :doc:`Services <../services>` and attach it to a ruleset.
2. In the target ruleset, add one rule with a single, simple action (for example,
   :doc:`Write to File <../../mwagentspecific/a-fileoptions>`).
3. Add filter conditions to narrow down the events:
   - Start broad (facility, severity, source)
   - Then add message/content filters
4. Add additional actions once the rule matches exactly what you intend.

Things that commonly trip people up
-----------------------------------

- Rule order matters: rules are evaluated top-to-bottom inside a ruleset.
- A service decides which ruleset sees an event. If events "disappear", verify the service-to-ruleset binding first.
- Defaults are templates. They do not process events until you create an actual service/action instance.

Next steps
----------

- Learn the core concepts: :doc:`Rules <../../glossaryofterms/rules>`.
- If you need to enrich events, see :doc:`Set Property <../../mwagentspecific/a-setproperty>`.
