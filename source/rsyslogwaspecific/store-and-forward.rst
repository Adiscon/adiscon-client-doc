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

Related analysis component
--------------------------

- For reviewing stored logs later, Adiscon LogAnalyzer works with file- and
  database-based storage.
- Users who prefer a simpler standalone tool for direct log file review may
  also consider the third-party log viewer
  `Retrospective <https://www.centeractive.com/products>`_ by centeractive.

Recommended setup path
----------------------

1. Start with one forwarding target and verify end-to-end delivery.
2. Prefer reliable transports when message loss is not acceptable.
3. Add internal actions only after the forwarding path behaves as expected.
4. If you need outage tolerance, configure disk-backed queues where the action
   supports it.

If stored data is reviewed later in a browser, treat Adiscon LogAnalyzer as a
separate downstream component. For the current split between service
administration and browser-based review, see
:doc:`../shared/faq/remote-administration-and-browser-based-review`.
