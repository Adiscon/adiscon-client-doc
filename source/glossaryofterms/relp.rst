
.. index:: RELP

RELP
====

RELP is the "Reliable Event Logging Protocol". It assures that no message is
lost in transit, not even when connections breaks and a peer becomes
unavailable. The current version of the RELP protocol has a minimal window of
opportunity for message duplication after a session has been broken due to
network problems. In this case, a few messages may be duplicated (a problem
that also exists with plain tcp syslog).


RELP addresses many shortcomings of the traditional plain tcp syslog protocol.
For some insight into that, please have a look at https://rainer.gerhards.net/2008/04/on-unreliability-of-plain-tcp-syslog.html.
Please note that RELP is currently a proprietary protocol. So the number of interoperable implementations is limited.


Note that for reliable operation where messages should be preserved over a
service shutdown, queue cache mode must be activated.
