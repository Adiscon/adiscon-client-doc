REGEX Compare Operation
=======================

The property will be evaluated against a regular expression. Everything known
in the regular expression syntax can be used to define a matching pattern.

Here are some regular expressions samples:

Regular Expression:

``[0-9]{4,4}-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}``

Matches typical Date like ``2018-11-20 12:11:01``


Regular Expression: ``\n[0-9]{4,4}``

Matches Linefeed and 4-digit number.



Regular Expression: ``(;|:)`` Matches semicolon or a colon.


More samples and details about the Regular Expression Syntax can be found here:

https://msdn.microsoft.com/en-us/library/bb982727(v=vs.90).aspx
