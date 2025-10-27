.. index:: Filter Conditions Boolean operators

Filter Conditions
=================

For every rule, filter conditions can be defined in order to guarantee that
corresponding actions are executed only at certain events.

These filter conditions are defined via logical operators. Boolean operators
like "AND" or "OR" can be used to create :doc:`complex filter conditions <../shared/references/complexfilterconditions>`.

If you are note so sure about the Boolean operators, you might find the
following brush-up helpful:


**AND** – all operands must be true for the result to be true. Example: AND (A, B):

Only if both A and B are true, the result of the AND operation is true. In all
other cases, it is false.

**OR** –  if at least one of the operands is true, the end result is also true.

Example: OR (A, B): The end result is only false if A and B are false.
Otherwise, it is true.

**XOR** –  it yields true if exactly one (but not both) of two operands is true.

Example: XOR (A, B): The end result is  false if A and B both are True or False.
Otherwise, it is true.

**NOT** – negates a value. Example: NOT A: If A is true, the outcome is false and

vice versa. There can only be a single operand for a NOT operation.

**TRUE** – returns true.

**FALSE** – returns false.
