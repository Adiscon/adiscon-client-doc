Rsyslog Windows Agent Tutorial
==============================

This tutorial is to provide an overview of Rsyslog Windows Agent and some of
its typical uses.

It is not a complete product documentary but helps enough to understand and
target the application according to your needs.

In the tutorial, we start by describing and focusing on the filter conditions,
as these are often needed to understand the usage scenarios that follow below.

Rsyslog Windows Agent gathers network events – or "information units" as we
call them – with its services.

Each of the events is then forwarded to a rule base, where the event is
serially checked against the different rule's filter conditions.

If such a condition evaluates to true ("matches"), actions associated with this
rule are carried out (for example, storing the information unit to disk or
emailing an administrative alert).


**Debug Logging**

When having Debug Logging enabled, the Username used for the Service will be
printed below the Version Build number now. This is useful for debugging
purposes.


.. toctree::
   :maxdepth: 1

   ../shared/gettingstarted/filterconditions
   ../rsyslogwaspecific/multiple-rulesets-rules-actions
   ../shared/gettingstarted/ignoringevents
   ../shared/gettingstarted/timebasedfilters
