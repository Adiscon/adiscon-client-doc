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

Common forwarding targets
-------------------------

- Syslog: :doc:`Forward Syslog <../mwagentspecific/a-forwardsyslogoptions>`
- SETP: :doc:`Forward via SETP <../mwagentspecific/a-forwardsetpoptions>`
- Email: :doc:`Send Email <../mwagentspecific/a-mailoptions>`

Recommended setup path
----------------------

1. Start with one local storage action so results are easy to inspect.
2. Add forwarding after filtering behaves the way you expect.
3. Test remote targets early so host, port, authentication, and protocol
   mismatches are found before production rollout.
