Difference between Set Status - Set Property Action
===================================================

The difference is, that a property is a part of the message object, while the
status is a global object. That means that a property will change with every
message, e.g. the timestamp or msg property. So properties are the actual
different values of a message. Values are gone once the message is fully
processed.

A status on the other hand is global and stays the same across all messages if
not altered. A status variable can be filtered, but its value cannot be emitted
in a message.

A setup for using a custom status object could be like this: Message "x" gets
processed every now and then. Every time the message comes through the status
variable "y" can be increased by 1. Once the status reaches a value of "n" a
special message with properties from message "x" can be sent via email and the
status variable "y" will be reset.

So, while setup looks similar, these are actually very different in their
concept.

1. Initializing 'status': This is usually done when needed in the processing
   flow with "Set Status".
2. How to set the status value again to initial value if I want to count up
   from the start: If you have a condition that waits for a specific status
   value to be reached, you can simply use another "Set Status" action after
   the output action.
3. Simple question: Status value should be numeral value? You can use numerical
   as well as alphabetical values for a status. But, I suppose it is best to
   only use something like boolean-like words when using alphabetical values,
   like on/off or yes/no. this is mostly because of logical understanding.
   Numerical values should be used for counters of course.
