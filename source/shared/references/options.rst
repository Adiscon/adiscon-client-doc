.. index:: Options

Options
=======

Options allow you to modify the contents of the property. Multiple options
can be set. They are comma-separated. If conflicting options are specified,
always the last option will be in effect (e.g. specifying "uppercase,lowercase"
will lead to lowercase conversion of the property value).

The following options are available with this release of the product:

**lowercase**

All characters in the resulting property extract will be converted to lower case.

**uppercase**

All characters in the resulting property extract will be converted to upper case.

**uxTimeStamp**

This is a special switch for date conversions. It only works if the extracted
property value is an ISO-like timestamp (YYYY-MM-DD HH:MM:SS). If so, it
will be converted to a Unix-like ctime() timestamp. If the extracted property
value is not an ISO-like timestamp, no conversion happens.

**uxLocalTimeStamp**

This is the same as uxTimeStamp, but with local time instead of GMT.

**date-rfc3339**

This option is for replacing the normal date format with the date format from
RFC3339.

**date-rfc3164**

This option is for replacing the normal date format with the date format from
RFC3164.

**date-rfc3164strict**

Does the same as date-rfc3164 but when the date is below 10, two spaces will be
added between Month and day (Which is defined in rfc3164).

**escapecc**

Control characters* in property are replaced by the sequence ``##hex-val##``, where* hex-val is the hexadecimal value of the control character (at least two digits,
may be more).

**spacecc**

Control characters* in the property are replaced by spaces. This option is most*
useful when a message contains control characters (e.g. a Windows Event Log
Message) and should be written to a log file.

**compressspace**

Compresses multiple consecutive space characters into a single one. The result
is a string where all words are separated by just single spaces.
To also compress control characters, use the compressspace and spacecc options
together (e.g.``'%msg:::spacecc,compressspace%'``). Please note that space compression happens on the final substring. So if you
use the FromPos and ToPos capabilities the substring is extracted first and
then the space compression applied. For example, you may have the msg string``"1  2"``. There are two space between 1 and 2. Thus, the property replacer expression:``%msg:1:3:compressspace%``

will lead to ``"1  "`` ('1' followed by two spaces). If you intend to receive
``"1 2"``('1' followed by one space, followed by '2'), you need to use ``%msg:1:4:compressspace%``

or

``%msg:1:/2/$:compressspace%``

In the second case, the exact length of the uncompressed string is not known,
thus a search is used in :doc:`topos <../references/topos>` to obtain it. The result is then
space-compressed.

**compsp**

Exactly the same as compressspace, just an abbreviated form for those that like
it brief.

**csv**

For example ``%variable:::csv%``. This option will create a valid CSV string. For example a string like this:``this is a "test"!`` becomes this ``"this is a ""test""!"``
where quotes are replaced with double quotes.

**cef**

Convert string content into valid McAfee CEF Format. This means that ``=``will be replaced with``\=`` and ``\`` will be replaced with ``\\``. **convgermuml**

Converts German Umlaut characters to their official replacement sequence
(e.g. "ö" --> "oe")

**localtime**

Now you can print the Time with localtime format by using``%variable:::localtime%``

**nomatchblank**

If this is used, the Property Replacer will return an empty string if the
:doc:`frompos <../references/frompos>` or :doc:`topos <../references/topos>` is not found.

**replacepercent**

This option replaces all ``%`` occurrences with a double ``%%``, which is needed for the property replacer engine in case that a string is reprocessed. This is
needed because the percent sign is a special character for the property
replacer. Once the property is processed, the double``%%``become automatically one``%``. **toipv4address**

Property string will be converted into IPv4 Address format if possible.

**toipv6address**

Property string will be converted into IPv6 Address format if possible.

**crlftovbar**

Does the same as date-rfc3164 but when the date is below 10, two spaces will be
added between Month and day (Which is defined in rfc3164).

**removecc**

Removes all control characters from 0x00 to 0x1F

**replacechar**

Replaces a single character with another single character.

How ASCII characters are being handled:

Sample:``%msg:$x:$y:replacechar%``

Broken down:

``%msg:$``<- Tells property replacer that a character is being expected (At the moment only for REPLACECHAR Option). ``x``<- The character to search for ``:``

``$``<- Tells property replacer that a character is being expected (At the moment only for REPLACECHAR Option). ``y``<- The character to replace with ``:``

``replacechar%``



How special characters are handled?

Sample: ``%msg:$\n:$|:replacechar%``

``%msg:$`` <- Tells property replacer that a character is being expected (At the moment only for REPLACECHAR Option). ``\n`` <- The character to search for special character, possible values: t for tab,

n for newline,

v for verticaltab,

f for formfeed,

r for carriage return

\ for an actual backslash.``:``

``$``<- Tells property replacer that a character is being expected (At the moment only for REPLACECHAR Option). ``|``<- The character to replace with ``:``

``replacechar%``


``*`` = control characters like e.g. carriage return, line feed, tab, ...*


**Important:** All option values are case-sensitive. So "uxTimeStamp" works
while "uxtimestamp" is an invalid option!
