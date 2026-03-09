Core concepts
=============

Use this section to understand how rsyslog Windows Agent thinks about
collected Windows events and how configuration objects interact.

Concept map
-----------

rsyslog Windows Agent processing follows this model:

1. A **service** collects or receives an event.
2. The collected data becomes an **information unit** inside the product.
3. The **rule engine** evaluates the event against **rules** and
   **filter conditions**.
4. Matching **actions** forward, transform, or discard the event.

Canonical concept pages
-----------------------

.. toctree::
   :maxdepth: 1

   rswaconcepts-services
   ../glossaryofterms/mwconcepts-informationunit
   ../glossaryofterms/rules
   ../glossaryofterms/ruleengine
   rswaconcepts-filterconditions
   rswaconcepts-actions

Why this matters
----------------

Understanding these concepts helps you:

- design rulesets with predictable behavior
- avoid duplicate or conflicting processing paths
- choose the right transport and action type for each receiver
- troubleshoot why an event did or did not match a rule
