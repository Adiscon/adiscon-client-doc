EventReporter filter conditions
===============================

Filter conditions define when a rule should match a collected Windows event.
They are the main way to separate high-value events from background noise.

A filter can be simple, such as one event ID check, or complex, with nested
Boolean logic across multiple properties.

A few key points matter:

- rule matching depends on the full filter expression
- an empty top-level condition matches everything
- filter order inside the Boolean tree affects the result
- precise filtering is usually easier if you first verify the broad event path
