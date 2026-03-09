.. _rsyslogwa-tour-store-and-forward:

Store and Forward
=================

Once rsyslog Windows Agent collects an event and it matches a rule, actions can
forward it to downstream systems or alter the processing flow internally.

Where to configure
------------------

- :doc:`Actions <actions>` is the entry point for forwarding and internal
  processing behavior.

Common forwarding targets
-------------------------

- Syslog: :doc:`Forward Syslog <a-forwardsyslogoptions>`
- RELP: :doc:`Send RELP <../mwagentspecific/a-sendrelp>`
- TLS-protected syslog: use the TLS options inside
  :doc:`Forward Syslog <a-forwardsyslogoptions>`
- DTLS: :doc:`Send DTLS <../mwagentspecific/a-senddtls>`

Common internal actions
-----------------------

- :doc:`Call RuleSet <../mwagentspecific/a-callruleset>`
- :doc:`Normalize Event <../mwagentspecific/a-normalizeevent>`
- :doc:`Set Property <../mwagentspecific/a-setproperty>`
- :doc:`Set Status <../mwagentspecific/a-setstatus>`
- :doc:`Discard <../mwagentspecific/a-discard>`

Recommended setup path
----------------------

1. Start with one forwarding target and verify end-to-end delivery.
2. Prefer reliable transports when message loss is not acceptable.
3. Add internal actions only after the forwarding path behaves as expected.
4. If you need outage tolerance, configure disk-backed queues where the action
   supports it.
