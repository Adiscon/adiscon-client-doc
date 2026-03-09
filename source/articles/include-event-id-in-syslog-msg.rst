:orphan:

Include Event ID in a Forwarded Syslog Message
==============================================

If you forward Windows Event Log data by syslog, the default output may not
show the Event ID in the exact place you want. You can include it explicitly in
several ways.

Recommended options
-------------------

1. **Use XML output**

   This is the best option when the receiving side can parse structured data.
   It preserves the full event details in a predictable format.

2. **Use a custom message format**

   In the :doc:`Forward Syslog action <../mwagentspecific/a-forwardsyslogoptions>`,
   define your own message format and insert the Event ID property where you
   want it. This is the best option when you need a specific flat-text layout.

3. **Use MoniLog-style output only if required**

   This older format can include the Event ID, but it is legacy behavior and is
   not the preferred choice for new setups.

4. **Change the Event Log Monitor output format only when you specifically need
   legacy behavior**

   This affects the event output earlier in the processing path and is usually
   less desirable than changing the Forward Syslog action itself.

Why this matters
----------------

Adding the Event ID to the forwarded message can help when the receiving system
expects plain-text identifiers for filtering, correlation, or display.

Related information
-------------------

* :doc:`../mwagentspecific/a-forwardsyslogoptions`
* :doc:`../mwagentspecific/eventlogmonitorv1`
* :doc:`../glossaryofterms/setp`
