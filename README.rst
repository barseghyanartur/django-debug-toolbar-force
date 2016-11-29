==========================
django-debug-toolbar-force
==========================
Show `django-debug-toolbar` in non- or partial-HTML views.

Installation
============
(1) Install latest stable version from PyPI:

.. code-block:: sh

    pip install django-debug-toolbar-force

(2) Add ``debug_toolbar_force.middleware.ForceDebugToolbarMiddleware`` to
    ``MIDDLEWARE_CLASSES`` of the your projects' Django settings (you would
    typically do that in your dev settings only).

.. code-block:: python

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'debug_toolbar_force.middleware.ForceDebugToolbarMiddleware',
    )

Usage
=====
In your browser, visit a non-HTML view and append ``?debug-toolbar`` at the
end.

.. code-block:: text

    GET http://localhost:8000/foo/json-view/?debug-toolbar

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
