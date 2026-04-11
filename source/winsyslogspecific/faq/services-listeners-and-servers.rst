:orphan:

.. _winsyslog-services-listeners-and-servers:

What do "service", "input", "listener", and "server" mean in WinSyslog?
========================================================================

Question
--------

In the WinSyslog documentation and GUI, what is the difference between a
``service``, an ``input``, a ``listener``, and a ``server``?

Answer
------

In WinSyslog, **service** is the main documentation term, and **input** is the
plain-language concept it represents.

- A **service** is a configured WinSyslog input that receives or generates
  events and sends them into a ruleset.
- An **input** is the easiest plain-language way to think about a receive-side
  service.
- A **listener** is the network-facing part of a service when the discussion is
  about IP address, port, transport, or TLS-related listen settings.
- A **server** usually appears because it is part of an existing GUI label,
  such as ``Syslog server`` or ``SETP Server``, or because WinSyslog is being
  described at the product level as a Windows syslog server.

If you want the simplest reading: think "add an input service that receives
logs", even when the GUI page is named ``Syslog server`` or ``RELP Listener``.

Details
-------

WinSyslog uses one Windows service process, but inside the product you can
configure multiple **services**. Each configured service has its own settings
and its own associated ruleset.

Some of those services are network inputs:

- ``Syslog server`` service receives syslog.
- ``RELP Listener`` service receives RELP.
- ``SETP Server`` service receives SETP.
- ``SNMP Trap Receiver`` service receives SNMP traps.

The GUI labels are technical and must stay exact in the documentation where
users need to match what they see on screen. That is why this manual keeps
names like ``Listener Port`` and ``Syslog server`` in field descriptions and
step-by-step UI instructions.

However, using only those labels can be hard for new users and for AI systems
that read the generated HTML. This manual therefore uses the following pattern:

- Use **service** as the default concept in prose.
- Read **service** as "configured input" when you want the clearest plain
  language.
- Use the exact GUI name the first time it matters, for example
  ``Syslog server`` service.
- Use **listener** only when the topic is network listen behavior, such as
  port conflicts, IP address selection, or TLS coexistence.
- Use **receiver** only for sender/receiver workflows where two systems are
  communicating.

This keeps the GUI terminology accurate while still making the operational role
easy to understand.

Action path
-----------

1. When you read a setup page, treat **service** as the main WinSyslog input
   concept and **input** as the plain-language meaning of that service.
2. When the GUI shows a specific label such as ``Syslog server`` or
   ``RELP Listener``, match that label exactly in the client.
3. When a page discusses port, IP address, or transport conflicts, read
   **listener** as "the network listen behavior of that service".
4. When a page discusses forwarding between two systems, read **sender** and
   **receiver** as the remote communication roles, not as different WinSyslog
   object types.

Related information
-------------------

- :doc:`../services`
- :doc:`../../shared/faq/listener-binding-rules`
