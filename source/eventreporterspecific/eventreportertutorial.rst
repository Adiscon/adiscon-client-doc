EventReporter Tutorial
======================

This tutorial provides a rough overview of EventReporter as well as some of its
typical uses. It is in no way complete, but helps in understanding
EventReporter and how it can be configured to suit your needs.

In the tutorial, we start by describing and focusing on the filter conditions,
as these are often needed to understand specified scenarios that follow below.

EventReporter gathers network events - or "information units" as we call them -
with its services. Each of the events is then forwarded to a rule base, where
the event is serially checked against the different rule's filter conditions.
If such condition evaluates to true ("matches"), actions associated with this
rule are carried out (e.g. storing the information unit to disk or emailing an
administrative alert).

**Note:** The screenshots in this tutorial are made with EventReporter and
MonitorWare Agent. MonitorWare Agent is used, as the user interface is similar
to the one EventReporter uses.


Debug Logging

When having Debug Logging enabled, the Username used for the Service will be
printed below the Version Build number now. This is useful for debugging
purposes.


.. toctree::
   :maxdepth: 1

   f-conditions
   ../eventreporterspecific/multiple-rulesets-rules-actions
   ../shared/gettingstarted/ignoringevents
   ../shared/gettingstarted/loggingevents
   ../shared/gettingstarted/timebasedfilters
   ../shared/gettingstarted/emailnotifications
   ../shared/gettingstarted/alarmingvianetsend
   ../shared/gettingstarted/startingscriptsandapplications
