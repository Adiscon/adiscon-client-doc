Core concepts
=============

Use this section to understand how EventReporter thinks about collected Windows
events and how configuration objects interact.

Concept map
-----------

EventReporter processing follows this model:

1. A **service** collects Windows Event Log data.
2. The collected data becomes an **information unit** inside EventReporter.
3. The **rule engine** evaluates the event against **rules** and
   **filter conditions**.
4. Matching **actions** store, forward, or transform the event.

Canonical concept pages
-----------------------

.. toctree::
   :maxdepth: 1

   erconcepts-services
   ../glossaryofterms/mwconcepts-informationunit
   ../glossaryofterms/rules
   ../glossaryofterms/ruleengine
   erconcepts-filterconditions
   ../glossaryofterms/mwconcepts-actions

Why this matters
----------------

Understanding these concepts helps you:

- design rulesets with predictable behavior
- avoid duplicate or conflicting processing paths
- choose the right action type for storage, forwarding, or alerting
- troubleshoot why an event did or did not match a rule
