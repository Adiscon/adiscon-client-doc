About rsyslog Windows Agent
===========================

**rsyslog Windows Agent collects Windows-originated events and forwards them to
rsyslog and other downstream receivers. It is built for Windows systems that
need reliable event forwarding, local filtering, and integration with Linux- or
rsyslog-centered logging environments.**

The product runs on the Windows systems that generate or relay events. It can
collect Windows Event Log data, monitor text-based log files, receive syslog
messages, and then process those events through rules before forwarding them.

rsyslog Windows Agent is especially useful when you want Windows systems to
feed a central rsyslog deployment with better structure and control than a
simple one-shot forwarder can provide. It supports syslog forwarding over UDP
and TCP, secure forwarding with TLS, and RELP for scenarios where reliable
transport matters.

The product is centered on two main runtime roles:

- the **rsyslog Windows Agent service**, which collects and forwards events in
  the background
- the **rsyslog Windows Agent Configuration Client**, which defines services,
  rulesets, filters, and forwarding actions

This manual covers installation, first-time setup, configuration, tutorials,
FAQ content, and reference material for rsyslog Windows Agent.

Manual
======

.. toctree::
   :maxdepth: 1

   rsyslogwaspecific/index
   Tutorials <rsyslogwaspecific/stepbystepguides>
   Configuration <rsyslogwaspecific/rsyslogwa>
   rsyslogwaspecific/faq
   Licensing and purchasing <shared/sales/index>
   Reference <rsyslogwaspecific/references>
   copyrights


* :ref:`genindex`
