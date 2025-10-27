# reStructuredText (RST) Syntax Rules for Agents

This document provides structured rules and guidelines for creating and editing reStructuredText (RST) files. It is designed to be used by AI agents and automated tools that work with RST documentation.

## Table of Contents

1. [Basic Principles](#basic-principles)
2. [Text Formatting](#text-formatting)
3. [Document Structure](#document-structure)
4. [Lists](#lists)
5. [Links and References](#links-and-references)
6. [Code and Literal Blocks](#code-and-literal-blocks)
7. [Tables](#tables)
8. [Directives](#directives)
9. [Images and Figures](#images-and-figures)
10. [Admonitions](#admonitions)
11. [Comments and Metadata](#comments-and-metadata)
12. [Common Pitfalls](#common-pitfalls)

## Basic Principles

### Indentation and Whitespace
- **RST is whitespace-sensitive** like Python
- Use consistent indentation (typically 3 or 4 spaces, no tabs)
- Blank lines are required between paragraphs and sections
- Multiple blank lines are treated as a single blank line
- First line of document is treated as if preceded by a blank line
- Last line of document is treated as if followed by a blank line

### Escaping
- Use backslash (`\`) to escape special characters
- In literal blocks, no escaping is needed
- In URIs, backslash-escaped whitespace represents a single space

## Text Formatting

### Inline Markup

| Markup | Syntax | Example | Result |
|--------|--------|---------|--------|
| Subscript | ``:sub:`text``` | ``:sub:`2``` | ₂ |
| Superscript | ``:sup:`text``` | ``:sup:`2``` | ² |

### Inline Markup Rules
1. **Cannot be nested** (e.g., `*You can't have **bold** inside italic*`)
2. Content **must not** start or end with whitespace: `* text*` is wrong
3. Must be separated from surrounding text by non-word characters
4. Use backslash-space for character-level markup: `long\ *ish*\ word`
5. The inline markup recognition rules are:
   - Start-string must be preceded by whitespace or specific punctuation
   - Start-string must be immediately followed by non-whitespace
   - End-string must be immediately preceded by non-whitespace
   - End-string must be followed by whitespace or specific punctuation
   - An end-string must be separated by at least one character from start-string
   - Unescaped backslash before markup disables recognition

## Document Structure

### Section Headers

Section headers are created by underlining (and optionally overlining) with punctuation characters:

```rst
================
Document Title
================

Chapter Title
=============

Section Title
-------------

Subsection Title
^^^^^^^^^^^^^^^^

Subsubsection Title
"""""""""""""""""""
```

#### Recommended Hierarchy
1. `#` with overline for parts
2. `*` with overline for chapters  
3. `=` for sections
4. `-` for subsections
5. `^` for subsubsections
6. `"` for paragraphs

#### Rules for Headers
- Underline must be at least as long as the title text
- If using overline and underline, they must be identical in length and character
- Valid section adornment characters: `! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~`
- Be consistent throughout the document

### Transitions

A transition marker is a horizontal line of 4 or more repeated punctuation characters:

```rst
Paragraph before transition.

----------

Paragraph after transition.
```

## Lists

### Bullet Lists

```rst
- First item
- Second item
  
  Continuation of second item
  
- Third item

* Can also use asterisk
+ Or plus sign
• Or bullet character (•)
```

Rules:
- Blank line required before first item
- Blank line required after last item
- Items must be consistently indented
- Text after bullet determines indentation

### Enumerated Lists

```rst
1. First item
2. Second item

a. Letter enumeration
b. Another item

i. Roman numerals
ii. Another item

#. Auto-numbered
#. Auto-numbered
```

Supported formats:
- Arabic numerals: `1, 2, 3...`
- Letters: `A, B, C...` or `a, b, c...`
- Roman numerals: `I, II, III...` or `i, ii, iii...`
- Auto-enumerator: `#`

### Definition Lists

```rst
Term
    Definition of the term, indented.
    
Term 2 : classifier
    Definition with optional classifier.

Term 3 : classifier one : classifier two  
    Multiple classifiers allowed.
```

## Links and References

### External Links

```rst
Standalone URL: https://example.com

Named link: `Link text <https://example.com>`_

Anonymous link: `Link text <https://example.com>`__
```

### Internal Links

```rst
.. _my-reference-label:

Section Title
=============

Refer to `my-reference-label`_ or :ref:`my-reference-label`

Link to section: `Section Title`_
```

### Footnotes

```rst
Text with footnote reference [1]_.

.. [1] This is the footnote text.

Auto-numbered footnote [#]_.
Named auto-number footnote [#note]_.

.. [#] Auto-numbered footnote.
.. [#note] Named footnote.
```

## Code and Literal Blocks

### Simple Literal Block

```rst
End a paragraph with double colon::

    This is a literal block.
    All whitespace is preserved.
```

### Code-Block Directive

```rst
.. code-block:: python
   :linenos:
   :emphasize-lines: 2,3
   :caption: Example code
   :name: example-code

   def hello(name):
       """Say hello."""
       print(f"Hello, {name}!")
```

Options:
- `:linenos:` - Show line numbers
- `:lineno-start: N` - Start line numbers at N
- `:emphasize-lines:` - Highlight specific lines
- `:caption:` - Add caption
- `:name:` - Reference name
- `:dedent:` - Remove indentation

### Inline Code

```rst
Use ``inline literals`` for code within text.

With role: :code:`inline code with syntax highlighting`
```

## Tables

### Simple Table

```rst
=====  =====  ======
A      B      A or B
=====  =====  ======
False  False  False
True   False  True  
False  True   True
True   True   True
=====  =====  ======
```

### Grid Table

```rst
+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span        |
+------------+-----------------------+
| body row 3 | - Cells may contain   |
|            | - Multiple items      |
+------------+-----------------------+
```

### CSV Table

```rst
.. csv-table:: Table Title
   :header: "Name", "Age", "Location"
   :widths: 30, 10, 30

   "Alice", 25, "New York"
   "Bob", 30, "Los Angeles"
```

## Directives

### Basic Directive Syntax

```rst
.. directive-name:: arguments
   :option1: value
   :option2: value

   Directive content goes here.
```

### Common Directives

#### Table of Contents

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents
   :numbered:
   :glob:

   introduction
   chapter*
   api/*
```

#### Include Directive

```rst
.. include:: other-file.rst

.. literalinclude:: code.py
   :language: python
   :lines: 1-10
```

#### Image Directive

```rst
.. image:: path/to/image.png
   :alt: Alternative text
   :width: 200px
   :align: center
```

#### Figure Directive

```rst
.. figure:: path/to/image.png
   :alt: Alternative text
   :width: 300px
   :align: center

   This is the figure caption.
```

## Admonitions

### Standard Admonitions

```rst
.. note::
   This is a note.

.. warning::
   This is a warning.

.. danger::
   This is a danger message.

.. tip::
   This is a tip.

.. important::
   This is important.

.. seealso::
   See also these references.

.. todo::
   This is a todo item (requires sphinx.ext.todo).
```

### Custom Admonition

```rst
.. admonition:: Custom Title

   Custom admonition content.
```

## Comments and Metadata

### Comments

```rst
.. This is a comment.
   It can span multiple lines.

..
   This is also a comment block.
```

### Substitutions

```rst
.. |name| replace:: replacement text

.. |logo| image:: logo.png
   :height: 20px

Use |name| in text, shows |logo| inline.
```

### Field Lists

```rst
:Author: John Doe
:Date: 2024-01-15
:Version: 1.0
```

## Common Pitfalls

### Indentation Errors
- **Wrong**: Inconsistent indentation in lists or directives
- **Right**: Use consistent spacing (3 or 4 spaces)

### Inline Markup Errors
- **Wrong**: `*bold *text*` (space after opening `*`)
- **Right**: `*bold text*`

### Missing Blank Lines
- **Wrong**: No blank line between paragraphs or before/after lists
- **Right**: Always separate blocks with blank lines

### Title Underline Too Short
- **Wrong**: Title text longer than underline
- **Right**: Underline at least as long as title

### Nested Inline Markup
- **Wrong**: `*italic with **bold** inside*`
- **Right**: Use roles or restructure text

### Unescaped Special Characters
- **Wrong**: Using `*` or `_` literally without escaping
- **Right**: `\*` or `\_` or use inline literals

### Reference Name Issues
- Names are case-insensitive and whitespace-normalized
- Use backquotes for phrase references: `` `phrase reference`_ ``
- Escape underscores in reference names: `name\_with\_underscore`

### Table Formatting
- Ensure column markers align properly
- Cell content must fit within column boundaries
- Use appropriate table type for content complexity

## Best Practices

1. **Be Consistent**: Use the same style throughout the document
2. **Use Semantic Markup**: Choose appropriate roles and directives
3. **Validate Often**: Check your RST syntax regularly
4. **Keep It Simple**: Don't over-complicate with excessive markup
5. **Document Structure**: Use clear hierarchy and organization
6. **Cross-References**: Use labels and references for navigation
7. **Version Control**: Track changes in documentation
8. **Preview Output**: Always check rendered output

## Sphinx-Specific Extensions

When using Sphinx, additional features are available:

### Domains and Roles
- `:doc:` - Link to other documents
- `:ref:` - Cross-reference to labels
- `:py:func:` - Python function reference
- `:class:` - Class reference
- `:meth:` - Method reference

### Special Directives
- `.. automodule::` - Auto-document Python modules
- `.. autoclass::` - Auto-document classes
- `.. autofunction::` - Auto-document functions
- `.. seealso::` - See also box
- `.. versionadded::` - Version information
- `.. deprecated::` - Deprecation notices

### Index Entries

```rst
.. index::
   single: term
   pair: term; definition
   triple: module; search; path
```

This comprehensive guide should help agents correctly parse, generate, and modify reStructuredText documents while avoiding common errors and following best practices.