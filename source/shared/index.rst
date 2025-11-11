:orphan:

Shared Content Library
======================

The ``shared`` directory centralizes documentation reused across multiple
Adiscon manuals. Organizing topics here avoids duplication and keeps each
product guide focused on unique behavior. This index also powers the
``make shared-html`` build target so the shared subset can be published
independently when needed.

.. important::

   Any shared page that references glossary or action anchors must begin with
   ``.. include:: ../shared/supporting-labels.rst`` so the common labels remain
   available wherever the page is included. Pages stored directly inside
   ``source/shared`` can alternatively point to ``.. include:: ../supporting-labels.rst``
   when that relative path is more convenient.

.. toctree::
   :maxdepth: 2

   gettingstarted/index
   references/index
   faq/mariadb-odbc-support
