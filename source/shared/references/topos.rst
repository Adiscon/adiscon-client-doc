.. index:: ToPos

ToPos
=====

If you do not want to use the full string from the property, you can specify
the highest character position to be copied here.


**Absolute Position**

Specify a simple integer if you would like to specify an absolute ending
position.


**Relative Position**

This is most useful together with the search capabilities of FromPos. A
relative position allows you to specify how many characters before or after the
FromPos you would like to have copied. Relative positions are specified by
putting a plus or minus ("+"/"-") in front of the integer.

Please note: if you specify a negative position (e.g. -20), FromPos and ToPos
will internally be swapped. That is the property value will not be (somehow)
reversely copied but they will be in right order. For example, if you specify
``%msg:30:-20%`` actually character positions 10 to 30 will be copied.

**Search Pattern**

Search pattern support is similar to search pattern support in FromPos.

A search pattern is specified as follows:

/<search-pattern>/<options>

If a search pattern is specified, the property value is examined and the first
occurrence of <search-pattern> is detected. The search is only carried out in
the string that follows FromPos. If the string is not found, nothing is
returned. If it is found, the position where the pattern is found is the ending
position or, if the option "$" is specified, the position immediately after the
pattern.

The search pattern may contain the "?" wildcard character, which represents any
character. Other wildcards are not supported with the property replacer.

Please note that a slash inside the search pattern will terminate the search
field. So pure slashes cannot be used. However, they can be escaped by
prefixing them with a backslash (\). The same applies to the '?' character. For
example, if you intend to search for ``"http://"`` inside a search pattern, you must use the following search string: ``"/http:////"``.

**Search Example**

A common use case is to combine searches in ToPos and FromPos to extract a
substring that is delimited by two other strings. To do so, use search patterns
in both fields. An example is as follows: assume a device might generate
message in the form ``"... error XXX occurred..."`` where "..." represents additional message text and XXX the actual error cause. You would like to extract the phrase ``"error XXX occurred"``. To do so, use the following property replacer syntax: ``%msg:/error/:/occurred/$/%``

Please note that the FromPos is used without the $-option, while in ToPos it is
used. If it hadn't been used in ToPos, only the part "error XXX " would have
been extracted, as the ToPos would point to the last character before the
search string.

Similarly, if only " XXX " should be extracted, the following syntax might be
used:

``%msg:/error/$:/occurred/%``

If you would also like to remove the spaces (resulting in just "XXX"), you must
include them into the search strings:

``%msg:/error /:/ occurred/$/%``


**Default**

If not specified, the ending position will be the last character.
