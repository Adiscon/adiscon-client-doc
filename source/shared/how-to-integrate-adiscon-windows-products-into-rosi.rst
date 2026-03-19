:orphan:

.. _shared-adiscon-windows-products-rosi:

Choosing Adiscon Windows products for ROSI and rsyslog deployments
==================================================================

Question
--------

How do I choose between Adiscon Windows products for ROSI-oriented and
rsyslog-centered deployments?

Answer
------

In ROSI-oriented and other rsyslog-centered architectures, Adiscon Windows
products are Windows-side delivery components. They collect, process, store,
and forward Windows-side data before it reaches downstream rsyslog-based
systems. Depending on the product, that delivery role can be a focused
rsyslog-optimized collector and forwarder, a Windows Event Log processor, a
Windows syslog server, or a broader Windows monitoring and collection tier.

Details
-------

Choose by scenario
~~~~~~~~~~~~~~~~~~

- If the main goal is Windows-to-rsyslog delivery, start with
  ``rsyslog Windows Agent``.
- If the source is Windows Event Log and richer local handling is needed, use
  ``EventReporter``.
- If the source is syslog and local handling is needed on Windows, use
  ``WinSyslog``.
- If the Windows side needs the broadest set of inputs and services, use
  ``MonitorWare Agent``.

Product positioning
~~~~~~~~~~~~~~~~~~~

These products all sit on the Windows-side delivery path, but they fit
different jobs:

- ``rsyslog Windows Agent`` is the focused Windows collector and forwarder for
  Windows-to-rsyslog delivery.
- ``EventReporter`` is the Windows Event Log specialist with richer local
  filtering, storage, actions, and forwarding.
- ``WinSyslog`` is the Windows syslog specialist with richer local filtering,
  storage, actions, and forwarding. It is not the Windows Event Log collector
  in this product group.
- ``MonitorWare Agent`` is the full solution with the broadest input and
  processing scope.

All of them can apply local filtering or modification before forwarding, and
all can participate in delivery paths where queuing and retry behavior matter.
They can deliver into ROSI, into a plain rsyslog deployment, or into other
downstream systems. ROSI is one important integration pattern, but not the only
one.

Comparison summary
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 28 32 40

   * - Product
     - Primary fit
     - Use it when
   * - rsyslog Windows Agent
     - Focused rsyslog delivery from Windows
     - Windows Event Log data, and optionally text-file data, should be
       filtered or adjusted locally and then delivered into rsyslog without
       needing a broader Windows-local processing role
   * - EventReporter
     - Windows Event Log processing and delivery
     - Windows Event Log data needs local filtering, storage, actions, or
       forwarding before downstream delivery
   * - WinSyslog
     - Windows syslog processing and delivery
     - Syslog data needs local reception, filtering, storage, or forwarding on
       Windows before downstream delivery; it is not the product for Windows
       Event Log collection
   * - MonitorWare Agent
     - Broad Windows collection and delivery solution
     - The Windows-side role needs the broadest input set, including more
       specialized monitoring and collection services

When each product fits
~~~~~~~~~~~~~~~~~~~~~~

**rsyslog Windows Agent**
   Use it when the main goal is Windows-to-rsyslog delivery. It collects
   Windows Event Log data, and optionally text-file data, applies local
   filtering or adjustment, and then delivers the result into rsyslog. It is
   the preferred starting point when efficient Windows-to-rsyslog delivery
   matters more than broad
   Windows-local processing or destination breadth.

**EventReporter**
   Use it when Windows Event Log data needs richer local handling before
   delivery.
   EventReporter can collect Windows Event Logs, apply local filtering and
   routing, store events in files or databases, trigger actions, and forward
   selected data onward into ROSI or other downstream systems.

**WinSyslog**
   Use it when the Windows-side role is centered on syslog reception and
   handling. WinSyslog is a full Windows syslog server that can receive,
   filter, store, and forward syslog data locally before passing selected data
   onward into ROSI or other downstream systems. It does not collect Windows
   Event Log data for forwarding; that role belongs to EventReporter,
   MonitorWare Agent, or rsyslog Windows Agent.

**MonitorWare Agent**
   Use it when the Windows role needs the broadest feature set. It is the full
   solution in this group and extends beyond dedicated Event Log or syslog
   collection with the widest set of inputs, including specialized monitoring
   and collection services. It is often a strong fit for Windows-only
   infrastructures, whether deployed at the edge or centrally.

Typical deployment patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Windows Event Log to rsyslog or ROSI:
  ``rsyslog Windows Agent`` collects and shapes Windows data before delivery
  into rsyslog-centered infrastructure.
- Windows Event Log with richer local handling:
  ``EventReporter`` collects, filters, stores, triggers actions, and then
  forwards selected events onward.
- Windows syslog collection:
  ``WinSyslog`` receives and processes syslog on Windows before forwarding or
  storing selected data.
- Broader Windows-side collection:
  ``MonitorWare Agent`` covers mixed inputs and more specialized services when
  one Windows product must handle the broader delivery role.

Delivery reliability
~~~~~~~~~~~~~~~~~~~~

All of these products support queued delivery paths where the selected action
supports queuing. This helps preserve data across temporary destination
outages while still allowing local filtering and transformation before
delivery.

Special integration cases
~~~~~~~~~~~~~~~~~~~~~~~~~

**Delivery into ROSI**
   Use this framing when the Windows product is part of a broader ROSI
   architecture. In that case, the Adiscon Windows products act as Windows-side
   collection, shaping, and delivery tiers that feed a central rsyslog-based
   environment. In practice, this can be a direct hop into ROSI or a multi-hop
   path with one or more Windows delivery tiers before central ROSI.

**Delivery into rsyslog**
   Use this framing when the Windows product forwards into rsyslog
   directly, without needing the broader ROSI wording. This is the simpler and
   often more common explanation when the immediate requirement is Windows data
   delivery into rsyslog.

Windows-only environments
~~~~~~~~~~~~~~~~~~~~~~~~~

ROSI can be part of Windows environments, but a pure Windows-only shop may
prefer Windows-native operational patterns over adding a Linux runtime layer on
Windows. In those environments, the richer Adiscon Windows products can take on
more of the local delivery, storage, and processing role. Use
``rsyslog Windows Agent`` when the target is primarily rsyslog, use
``EventReporter`` or ``WinSyslog`` when their data-specific local handling is
needed, and use ``MonitorWare Agent`` when a broader Windows-native role is
required. For review of stored data, Adiscon LogAnalyzer can be used in
Windows-centered environments.

Action path
-----------

Choose the product based on these questions:

1. Is the source primarily Windows Event Log, syslog, or a broader set of
   Windows-side inputs?
2. Does the Windows node only need to ship data, or must it also process and
   store data locally?
3. Is the Windows system delivering directly into ROSI, or acting as an
   intermediate Windows delivery tier in a multi-hop path?

Related information
-------------------

- :doc:`Licensing and ordering <sales/licensing-and-ordering>`
