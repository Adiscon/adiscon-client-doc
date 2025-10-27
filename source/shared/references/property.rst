.. index:: Property

Property
========

This is the name of the property to be replaced. It can be any property that a
given event possesses. If a property is selected that is empty for the event
processed, an empty string is returned.

A property is either an :doc:`event property <../references/eventproperties>`, a
:doc:`custom property <../references/customproperties>`, a dynamic property
or a :doc:`system property <../references/systemproperties>`.

If a property is selected that is not present, the result will always be an
empty string, no matter which other options have been selected.
