Process and Filter
==================

MonitorWare Agent processes incoming monitoring data in a consistent sequence:

1. a service produces an information unit
2. the information unit enters the assigned ruleset
3. each rule evaluates its filter conditions
4. matching rules execute their actions in order

Use broad rules first, then narrow them with filters once the data flow is
verified.

What to filter on
-----------------

The available filter fields depend on the service type. Typical examples are:

- event ID, source, level, and channel for Event Log Monitor services
- sender, facility, and severity for syslog input
- response status or measured values for probe services
- filename, content, or custom properties for file-based monitoring

Start simple
------------

For a new deployment, prefer one of these first:

- one broad collection rule with one output action
- one broad collection rule plus one targeted alert rule

This avoids hiding configuration errors behind overly complex filters.

Related configuration topics
----------------------------

- :doc:`filterconditions`
- :doc:`../shared/references/complexfilterconditions`
- :doc:`../glossaryofterms/rules`
