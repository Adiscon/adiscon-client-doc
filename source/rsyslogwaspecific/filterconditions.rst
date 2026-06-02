.. index:: Filter Conditions

Filter Conditions
=================

Filter conditions specify **when** a rule should run. If the filter condition
evaluates to true, the actions in that rule are executed.

In practice, filters let you decide which Windows events should be forwarded,
which should be routed differently, and which should be ignored.

How to use them well
--------------------

- Start with broad filters so the event path is easy to verify.
- Narrow down with event source, event ID, severity, or log name.
- Add message-content filters only after the basic event path works.
- Remember that rule order matters just as much as the filters themselves.

Detailed filter references
--------------------------

.. toctree::
   :maxdepth: 2

   ../mwagentspecific/f-globalconditions
   ../mwagentspecific/f-dateconditions
   ../mwagentspecific/f-operators
   ../mwagentspecific/f-filters

Basic filters
-------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/f-general
   ../mwagentspecific/f-datetime
   ../mwagentspecific/f-informationunittype

Network-related filters
-----------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/f-syslog

Windows and file monitoring filters
-----------------------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/f-eventlogmonitorv1
   ../mwagentspecific/f-eventlogmonitorv2
   ../mwagentspecific/f-filemonitor

Custom properties
-----------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/f-customproperty
   ../mwagentspecific/f-extendednumberproperty
   ../mwagentspecific/f-extendedipproperty
   ../mwagentspecific/f-fileexists
   ../mwagentspecific/f-storefilterresults
