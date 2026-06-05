.. _eventreporter-tour-store-and-forward:

Store and Forward
=================

Once EventReporter collects an event and it matches a rule, actions can store
it locally or forward it to downstream systems.

Where to configure
------------------

- :doc:`Actions <actions>` is the entry point for output, storage, and
  notification behavior.

Common storage targets
----------------------

- Flat files: :doc:`Write to File <../mwagentspecific/a-fileoptions>`
- Databases: :doc:`Write to Database <../mwagentspecific/a-databaseoptions>`
- Windows Event Log: :doc:`Write to Event Log <../mwagentspecific/a-eventlogoptions>`

Database setup paths
--------------------

- Default supported schema: :doc:`tutorial-database-logging`
- Custom schema integration: :doc:`tutorial-custom-database-integration`

Common forwarding targets
-------------------------

- Syslog: :doc:`Forward Syslog <../mwagentspecific/a-forwardsyslogoptions>`
- SETP: :doc:`Forward via SETP <../mwagentspecific/a-forwardsetpoptions>`
- Email: :doc:`Send Email <../mwagentspecific/a-mailoptions>`

Related analysis component
--------------------------

- For reviewing stored logs later, Adiscon LogAnalyzer works with file- and
  database-based storage.
- Users who prefer a simpler standalone tool for direct log file review may
  also consider the third-party log viewer
  `Retrospective <https://www.centeractive.com/products>`_ by centeractive.

Recommended setup path
----------------------

1. Start with one local storage action so results are easy to inspect.
2. Add forwarding after filtering behaves the way you expect.
3. Test remote targets early so host, port, authentication, and protocol
   mismatches are found before production rollout.

For browser-based review of stored data, use Adiscon LogAnalyzer as a separate
component. For the current split between service administration and
browser-based review, see
:doc:`../shared/faq/remote-administration-and-browser-based-review`.
