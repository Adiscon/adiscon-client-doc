Core concepts
=============

Use this section to understand how WinSyslog thinks about incoming events and
how configuration objects interact. These pages are the conceptual backbone for
input services, rulesets, filters, and actions.

If you are new to the product, read this section after ``Getting Started`` and
before deep configuration work.

Concept map
-----------

WinSyslog processing follows this model:

1. An **input service** receives or generates an event.
2. The event becomes an **information unit** inside WinSyslog.
3. The **rule engine** evaluates the event against **rules** and
   **filter conditions**.
4. Matching **actions** store, forward, display, or transform the event.

In plain language, you can read this as:

``input service -> ruleset -> action``

Canonical concept pages
-----------------------

.. toctree::
   :maxdepth: 1

   wsconcepts-services
   ../glossaryofterms/mwconcepts-informationunit
   ../glossaryofterms/rules
   ../glossaryofterms/ruleengine
   wsconcepts-filterconditions
   ../glossaryofterms/mwconcepts-actions

Why this matters
----------------

Understanding these concepts helps you:

- design rulesets with predictable behavior for each input service
- avoid duplicate or conflicting processing paths
- choose the right action type for storage, forwarding, or alerting
- troubleshoot why an event did or did not match a rule
