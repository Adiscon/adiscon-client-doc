:orphan:

.. _user-interface-changes:

User Interface changes
======================

The **26.07** installer includes the established configuration client and the
new user interface for this product:

- **Established configuration client** - the WinForms client documented in this
  manual and the primary reference for setup steps and screenshots.

.. only:: winsyslog or winsyslog_j

   - **WinSyslog User Interface** - the newer WinUI-based interface
     (``adiscon-client-ng``) available alongside the established configuration
     client.

.. only:: eventreporter

   - **EventReporter User Interface** - the newer WinUI-based interface
     (``adiscon-client-ng``) available alongside the established configuration
     client.

.. only:: mwagent

   - **MonitorWare Agent User Interface** - the newer WinUI-based interface
     (``adiscon-client-ng``) available alongside the established configuration
     client.

.. only:: rsyslog

   - **rsyslog Windows Agent User Interface** - the newer WinUI-based interface
     (``adiscon-client-ng``) available alongside the established configuration
     client.

The established configuration client supports license file application and full
configuration editing. See your product website's **Upgrade** article for the
customer-facing description of the product-specific user interface.

Property window toolbar
-----------------------

When you open a service or action property window, the toolbar provides
**Save**, **Verify Configuration**, **Connect**, **Start**, **Stop**,
**Restart**, **Reset Changes**, and **Quit**. **Reset Changes** discards
unsaved edits on the open form only; it does not restore factory defaults for
the selected item.

.. image:: ../../images/service-toolbar-2026.png
   :width: 100%

The **main window** (rules tree) has a separate toolbar with **Start**,
**Stop**, **Restart**, **Kill**, and **Open Windows Services** for the
background service. **Kill** ends an orphan process when the service manager
state is inconsistent. **Open Windows Services** opens ``services.msc`` for
Windows Service management.

When the service is **paused** during configuration reload, stop and restart
may be disabled until reload completes.

Reset configuration to default
------------------------------

The **File** menu provides **Reset Configuration to Default**, which resets the
whole deployed configuration:

.. image:: ../../images/reset-to-default-menu.png
   :width: 100%

This is separate from **Reset Changes** on an open property form. It is also
separate from the context menu or toolbar **Reset** command for a selected
service or action, which restores only that selected item to factory defaults.

Event Viewer
------------

After start, stop, or configuration reload, service-management events are
prepended in the Event Viewer so recent control actions appear at the top.

File formats
------------

The **File** menu supports:

.. only:: mwagent

   .. image:: ../../images/file-menu-yaml-mwagent.png
      :width: 100%
      :alt: MonitorWare Agent File menu with YAML import and export commands

   *MonitorWare Agent File menu with YAML import and export commands*

.. only:: winsyslog or winsyslog_j

   .. image:: ../../images/file-menu-yaml-winsyslog.png
      :width: 100%
      :alt: WinSyslog File menu with YAML import and export commands

   *WinSyslog File menu with YAML import and export commands*

.. only:: eventreporter

   .. image:: ../../images/file-menu-yaml-eventreporter.png
      :width: 100%
      :alt: EventReporter File menu with YAML import and export commands

   *EventReporter File menu with YAML import and export commands*

.. only:: rsyslog

   .. image:: ../../images/file-menu-yaml-rsyslog.png
      :width: 100%
      :alt: rsyslog Windows Agent File menu with YAML import and export commands

   *rsyslog Windows Agent File menu with YAML import and export commands*

- **Adiscon YAML Config Format** (``.yaml``) - import and export
- **Adiscon Legacy Format** (``.cfg``) - legacy text configuration

See the file-based configuration chapter in your product manual and
:ref:`unsupported-configuration-blocks`.

Related information
-------------------

- :ref:`version-numbering-change`
