.. index:: FromPos

FromPos
=======

If you do not want to use the full string from the property, you can specify a
start position here. There are two ways to specify the start location:


**Fixed Character position**

If you know exactly on which position the string of interest begins, you can
use a fixed location. In this case, simply specify the character position
containing the first character of interest. Character positions are counted
at 1.


**Search Pattern**

A search pattern is specified as follows:

/<search-pattern>/<options>


If a search pattern is specified, the property value is examined and the first
occurrence of <search-pattern> is detected. If it is not found, nothing is
returned. If it is found, the position where the pattern is found is the start
position or, if the option "$" is specified, the position immediately after the
pattern.

The search pattern may contain the "?" wildcard character, which represents any
character. Other wildcards are not supported with the property replacer.

Please note that a slash inside the search pattern will terminate the search
field. So pure slashes cannot be used. However, they can be escaped by
prefixing them with a backslash (\). The same applies to the '?' character. For
example, if you intend to search for ``"http://"`` inside a search pattern, you must use the following search string: ``"/http:////"``.


**Default Value**

If the FromPos is not specified, the property string is copied starting at
position 1.
