:orphan:

.. _unsupported-configuration-blocks:

What happens when the client opens a configuration with unsupported blocks?
===========================================================================

Question
--------

The configuration client shows a warning about unsupported configuration items
when I open a file. What does that mean?

Answer
------

The client skipped configuration blocks that this client version does not
understand. Saving the configuration may remove those unsupported sections.

Details
-------

Newer service or file formats can introduce configuration blocks (for example
``general(name="Metrics")``) that an older configuration client cannot edit.
The client loads what it supports and displays a one-time warning.

If you save without upgrading the client, unsupported blocks may be dropped from
the saved file.

Action path
-----------

1. Note which blocks the warning mentions.
2. If you need to edit those settings, upgrade to a configuration client that
   supports them, or edit the YAML or legacy ``.cfg`` file with care in a text
   editor.
3. Back up the configuration before saving from an older client.

Related information
-------------------

- See the file-based configuration chapter in the WinSyslog, EventReporter,
  MonitorWare Agent, or rsyslog Windows Agent manual.
