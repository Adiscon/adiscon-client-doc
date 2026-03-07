.. _winsyslog-tour-store-and-forward:

Store and Forward
=================

Once WinSyslog receives an event and it matches a rule, actions can store it
locally and forward it to downstream systems.

Where to configure
------------------

- :doc:`Actions <../actions>` is the entry point for all output and notification options.

Common storage targets
----------------------

- Flat files: :doc:`Write to File <../../mwagentspecific/a-fileoptions>`
- Databases: :doc:`Write to Database <../../mwagentspecific/a-databaseoptions>`
- Windows Event Log: :doc:`Write to Event Log <../../mwagentspecific/a-eventlogoptions>`

Common forwarding targets
-------------------------

- Syslog: :doc:`Forward Syslog <../a-forwardsyslogoptions>`
- SETP: :doc:`Forward via SETP <../../mwagentspecific/a-forwardsetpoptions>`
- Email: :doc:`Forward via Email <../../mwagentspecific/a-mailoptions>`
- Interactive viewing: forward messages to :doc:`../../interactivesyslogviewer/index`
  if you want to see incoming data live in the Interactive Syslog Viewer.

Related analysis component
--------------------------

- For reviewing stored logs later, Adiscon LogAnalyzer works with file- and
  database-based storage.

Recommended setup path
----------------------

1. Start with one storage action (file or database) to verify your rules.
2. Add a forwarding action after you are confident filtering is correct.
3. If you forward to a remote target, test connectivity and credentials early.

Next steps
----------

- If you need reliable ingestion on the input side, see :doc:`RELP listener <../../mwagentspecific/relplistener>`.
