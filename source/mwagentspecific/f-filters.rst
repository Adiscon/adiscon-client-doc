Filters
=======

Filters can be added under each Operation node. There are a few common filters
which can be used for all services and there are special filters which only
apply if a special kind of Information Unit is evaluated.


**What happens with Filters that are not available in an "Information Unit"?**

Every filter that is not found in an Information Unit is ignored in the
filtering process. If you want to create filters specialized for types of
Information Units, always make sure to add an "Information Unit Type" filter.

An example, you have one ruleset, rule and action. In the filters you have one
EventID filter. Then you have two services, one Eventlog Monitor and the other
is Heartbeat monitor both pointing to this ruleset. The Information Units from
the Eventlog Monitor would be filtered correctly, but those from the Heartbeat
monitor would not be filtered as they do not have an EventID property. The
EventID filter would be ignored and the actions would be executed every time.

**Note, if a filter is used that does not apply to the evaluated Info Unit, it will be just ignored. This gives you the possibility to build one filter set for several types of Information Units.**

There are different types of filters, and so there a different ways in which
you can compare them to a value. The following Types exist:


**String:**
  Can be compared to another String with "=", "Not =", "Range Match" or through

  .. toctree::
     :maxdepth: 1

     regex



**number:**
  can be compared with another number with "=", "not =", "<" and ">"


**boolean:**
  can be compared to either true or false with "=" and "not ="


**time:**
  can be compared with another time but only with "="

  the list of possible filters, which can be evaluated is described in the
  following sections.
