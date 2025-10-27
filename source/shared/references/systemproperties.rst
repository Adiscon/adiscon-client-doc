.. index:: System Properties

System Properties
=================

System properties are special sequences that can be helpful. They are available
with all event types. They are:

**$CRLF**

A Windows newline sequence consisting in the characters CR and LF. If you just
need CR, you can use ``%$CRLF:1:1%`` and if you need use LF you can use ``%$CRLF:2:2%``

**$TAB**

An US-ASCII horizontal tab (HT, 0x09) character

**$HT**

same as $TAB

**$CR**

A single US-ASCII CR character (shortcut for ``%$CRLF:1:1%``) **$LF**

A single US-ASCII LF character (shortcut for``%$CRLF:2:2%``) **$xNN**

A single character, whose value (in hexadecimal) is given by NN. NN must be two
hexadecimal digits - a leading zero must be used if a value below 16 is to be
represented. The value 0 (%x00) is invalid and - if specified - replaced by the
"?" character.

As an example, $CR could also be expressed as %$x0d%.

Please note that only one character can be represented. If you need to specify
multiple characters, you need multiple $xNN sequences. An example may be $CRLF
which could also be specified as %$x0d%%$x0a% (but not as %$x0d0a%).

**$NOW**

Contains the current date and time in the format:``YYYY-MM-DD HH.MM.SS``

Please note that the time parts are delimited by ``'.'`` instead of ``':'``. This makes the generated name directly suitable for file name generation.

If you need just parts of the timestamp, please use the property replacer's
substring functionality to obtain the desired part. Use``%$NOW:1:4% to get the year,``

``%$NOW:6:7% to get the month,``

...

``%$NOW:1:10% to get the full datestamp,``

``%$NOW:12:20% to get the full timestamp``

**$NEWUUID**

Creates a new UUID (Universally Unique Identifiers), a unique 128-bit integer
represented as a 32 digit hexadecimal number.
