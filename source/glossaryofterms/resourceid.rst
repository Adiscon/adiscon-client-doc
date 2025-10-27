
.. index:: Resource ID

Resource ID
===========

The Resource ID is an identifier used by the :doc:`adiscon's monitorware line of products <../glossaryofterms/mwlineofproducts>`.
It is a simple, administrator assigned string value. It can be used to correlate
different events - even from different source - to a specific resource.

For example, on a Windows server running Microsoft Exchange, all Exchange
events could be assigned to a resource id of "Exchange Server".

In `MonitorWare Agent <https://www.mwagent.com/>`_ and `WinSyslog <https://www.WinSyslog.com/>`_ support for Resource IDs is limited. The
field is present and can be persisted to the database or stored in XML files,
but besides this there is no value in it.
