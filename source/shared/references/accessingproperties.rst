.. index:: Accessing Properties

Accessing Properties
====================

Properties are accessed by their name. The component used for this is called
the "property replacer". It is a generic component that allows you to merge
properties from the event processed to e.g. the email subject line or a log
file line. It is a central component that is used as often in the product as
possible. The idea behind the property replacer is that there is often need to
specify a value from the event processed.

The property replacer provides very powerful ways to access the properties: they
cannot only be accessed as one full property. They can also be accessed as
substrings and even be reformatted. As such, the property replacer provides a
specific syntax to access properties:

``%property:fromPos:toPos:options%``

The percent-signs ("%") indicate the start of a special sequence. The other
parameters have the following meanings

FromPos and ToPos can be used to copy a substring from a lengthy property. The
options allow to specify some additional formatting.

Within the properties, all time is based on UTC regardless if your preferred
time is UTC or localtime. So if you want to display localtime instead of UTC,
you have to use the following syntax: ``%variable:::localtime%``

.. toctree::
   :maxdepth: 1

   property
   frompos
   topos
   options
   examples
