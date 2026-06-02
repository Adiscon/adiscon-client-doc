rsyslog Windows Agent Actions
=============================

Actions define what happens after an event matches a rule.

Forwarding actions
------------------

The main forwarding actions in rsyslog Windows Agent are:

- **Forward Syslog** for standard syslog delivery over UDP or TCP
- **Send RELP** for reliable event transport to a RELP-enabled receiver
- **Send DTLS** for packet-based transport with encryption where that is required

Internal actions
----------------

Internal actions modify or redirect processing inside the agent itself:

- **Call RuleSet** transfers processing to another ruleset
- **Normalize Event** rewrites selected event content
- **Set Property** and **Set Status** add or modify internal values
- **Discard** stops further processing for the current event

Why order matters
-----------------

Actions run in the order you place them inside a rule. That order affects both
event content and delivery behavior.
