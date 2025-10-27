Simple Examples
===============

A good example for this is the email subject line, which has severe length
constraints. If you would like to have only the first 40 characters of the
actual message text in the subject, you could use the replacer: ``"%msg:1:40%"``. If you know the first 10 characters of the message are meaningless for you but
you would  like to see the full rest of the message (no matter how long it may
be), you can use a sequence like ``"%msg:11%"``.

If you would just like to see the plain message from beginning to end, you can
simply omit :doc:`frompos <../references/frompos>` and
:doc:`topos <../references/topos>`: ``"%msg"``. Of course, all of these sample not only work with the "msg" property, but also
with all others like "facility", or "priority", or W3C-log header extracted
property names.


**More complex Examples**

If you would like to extract the 50 characters from the message after the word
DROP, you would use the following replacer string:``%msg:/DROP/$:+50%``

If you would like to have the first 40 characters in front of the string "-
aborted" (including that string):

``%msg:/- aborted/$:-40%``

If you would like to receive everything starting from (and including) "Log:":

``%msg:/Log/%``

If you would like to have everything between the string "FROM" and "TO"
including NONE of the both searchstrings:

``%msg:/FROM/$:/TO/%``

If you would just like to log lowercase letters in your log messages:

``%msg:::lowercase%``

And if you would just like to have the first 50 characters (and these in lower
case):

``%msg:50:::lowercase%``

If you need to change a timestamp to a UNIX-like timestamp, you could use this:

``%datereceived:::uxTimeStamp%``

Please see also the focused sample in the :doc:`topos <../references/topos>` description.


**A real world Sample**

We use the following template to generate output suitable as input for MoniLog:

``%timegenerated:1:10%,%timegenerated:12:19%,%source%,%syslogfacility%,%syslogprio rity%,EvntSlog: %severity% %timereported:::uxTimeStamp%: %source%/%sourceproc% (%id%) - "%msg%"%$CRLF%``

**Please note: everything is on one line with no line breaks in between. This**
example is from the "write to file" action (with custom file format).**
