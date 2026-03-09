EventReporter services
======================

Services inside EventReporter gather the Windows event data that is processed
by rules. Each service type represents a collector with its own settings and
behavior.

EventReporter is primarily built around Windows Event Log collection. In most
installations, the active services are one or more Event Log Monitor instances.

A few key points matter:

- there can be multiple service instances as long as their settings do not
  conflict
- each service instance is bound to a ruleset
- service defaults are only templates, not active collectors
- if no service is configured, EventReporter does not collect any events
