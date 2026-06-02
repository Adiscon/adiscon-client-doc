rsyslog Windows Agent Filter Conditions
=======================================

Filter conditions decide whether a rule matches an event.

What they are for
-----------------

Use filter conditions to separate the events you care about from the ones you
do not want to forward, enrich, or route further.

Typical filter categories
-------------------------

- **Global Conditions** such as minimum wait time or event occurrence count
- **General Conditions** such as source system or message content
- **Date / Time** constraints for business-hour or schedule-based logic
- **Information Unit Type** to separate event log, syslog, or file-based data
- **Syslog** properties such as facility or priority
- **Event Log Monitor** properties such as event ID, event source, severity,
  category, or user
- **Custom Property** conditions for enriched or generated values

Recommended approach
--------------------

Start simple. First verify that the event reaches the intended ruleset. Then
add the smallest set of filters needed to narrow the match.
