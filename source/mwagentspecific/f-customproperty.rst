Custom Property
===============

Custom Property specific filter is described here.


.. only:: mwagent

   .. image:: ../images/f-customproperty-mwagent.png
      :width: 100%
      :alt: MonitorWare Agent Add Filter menu with the Custom Property filter

   *MonitorWare Agent Filter Conditions - Custom Property*

.. only:: winsyslog or winsyslog_j

   .. image:: ../images/f-customproperty-winsyslog.png
      :width: 100%
      :alt: WinSyslog Add Filter menu with the Custom Property filter

   *WinSyslog Filter Conditions - Custom Property*

.. only:: eventreporter

   .. image:: ../images/f-customproperty-eventreporter.png
      :width: 100%
      :alt: EventReporter Add Filter menu with the Custom Property filter

   *EventReporter Filter Conditions - Custom Property*

.. only:: rsyslog

   .. image:: ../images/f-customproperty-rsyslog.png
      :width: 100%
      :alt: rsyslog Windows Agent Add Filter menu with the Custom Property filter

   *rsyslog Windows Agent Filter Conditions - Custom Property*


**Custom Property**
  As the name suggests it is a "Custom Property". Internally in MonitorWare Agent
  all values are stored in properties. For example the main message is stored in
  a property called "msg". By using this dialog you can access properties which
  are dynamic (Like those from SNMP Trap Monitor when using V2 protocol).

  This filter is of type string.
