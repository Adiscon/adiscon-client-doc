
.. index:: Syslog Facility

Syslog Facility
===============

Syslog Facility is one information field associated with a syslog message. It
is defined by the `Syslog <https://www.adiscon.com/syslog/>`_ protocol. It is
meant to provide a very rough clue from what part of a system the message
originated from. Traditionally, under UNIX, there are facilities like KERN
(the OS kernel itself), LPD (the line printer daemon), and so on. There are also
the `LOCAL_0` to `LOCAL_7` facilities, which were traditionally reserved for
administrator and application use.

However, with the wide adoption of the syslog protocol, the facility field
contents has become a little less clear. Most syslog enabled devices nowadays
allow configuring any value as the facility. So it is basically left to
distinguish different classes of syslog messages.

The facility can be very helpful to define rules that split messages for
example to different log files based on the facility level.
