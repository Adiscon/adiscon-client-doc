Multiple RuleSets - Rules - Actions
===================================


.. image:: ../../images/multiple-rulesets-rules-actions.png
   :width: 100%

* Multiple RuleSets, Rules and Actions*

With the MonitorWare Agent as many "RuleSets", "Rules" and "Actions" as
necessary can be defined.

You can create a separate "RuleSet" for each :doc:`service <../../glossaryofterms/mwconcepts-services>` used, or just one
"RuleSet" for all Services. RuleSets can also be created to use them with the
:doc:`"callruleset action" <../../mwagentspecific/a-callruleset>`.

RuleSets contain one or multiple :doc:`rules <../../glossaryofterms/rules>`. All Actions and processing carried
out is defined by the Rules.
A Rule consists of :doc:`filter conditions <../../glossaryofterms/mwconcepts-filterconditions>` and 1 to
multiple :doc:`actions <../../glossaryofterms/mwconcepts-actions>`.
All Actions that have to meet the same Filter Conditions can be combined in the same Rule.
