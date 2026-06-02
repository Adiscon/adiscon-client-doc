.. index:: Services

Services
========

Services are the configured EventReporter inputs. They collect Windows event
data and pass it to rulesets for further processing.

In EventReporter, the most important service types are the Windows Event Log
monitor services. They read Windows events and make them available to the rule
engine.

In this manual, **input** is the clearest plain-language concept, while
**service** remains the operational term for the configured EventReporter
object.

Important behavior
------------------

- You must define at least one input service, otherwise EventReporter has no
  event data to process.
- A service instance is an active collector.
- A service default is only a template. It does not collect anything until you
  create an actual service instance from it.
- Each service instance is bound to one ruleset.

Service types used in EventReporter
-----------------------------------

.. toctree::
   :maxdepth: 1

   ../mwagentspecific/heartbeat
   ../mwagentspecific/monitorwareechoreply
   ../mwagentspecific/eventlogmonitorv1
   ../mwagentspecific/eventlogmonitorv2
