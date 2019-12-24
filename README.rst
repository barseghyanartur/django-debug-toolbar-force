==========================
django-debug-toolbar-force
==========================
Show ``django-debug-toolbar`` in non- or partial-HTML views.

.. image:: https://img.shields.io/pypi/v/django-debug-toolbar-force.svg
   :target: https://pypi.python.org/pypi/django-debug-toolbar-force
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/django-debug-toolbar-force.svg
    :target: https://pypi.python.org/pypi/django-debug-toolbar-force/
    :alt: Supported Python versions

.. image:: https://img.shields.io/travis/barseghyanartur/django-debug-toolbar-force/master.svg
   :target: http://travis-ci.org/barseghyanartur/django-debug-toolbar-force
   :alt: Build Status

.. image:: https://readthedocs.org/projects/django-debug-toolbar-force/badge/?version=latest
    :target: http://django-debug-toolbar-force.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-GPL--2.0--only%20OR%20LGPL--2.1--or--later-blue.svg
   :target: https://github.com/barseghyanartur/django-debug-toolbar-force/#License
   :alt: GPL-2.0-only OR LGPL-2.1-or-later

.. image:: https://coveralls.io/repos/github/barseghyanartur/django-debug-toolbar-force/badge.svg?branch=master
    :target: https://coveralls.io/github/barseghyanartur/django-debug-toolbar-force?branch=master
    :alt: Coverage

Prerequisites
=============
- Python 2.7, 3.5, 3.6, 3.7 and 3.8.
- Django 1.8, 1.9, 1.10, 1.11, 2.0, 2.1, 2.2 and 3.0.
- django-debug-toolbar 1.5 (may work on earlier versions as well, although
  not guaranteed).

Documentation
=============
Documentation is available on `Read the Docs
<http://django-debug-toolbar-force.readthedocs.io/>`_.

Installation
============
(1) Install latest stable version from PyPI:

    .. code-block:: sh

        pip install django-debug-toolbar-force

    or latest stable version from GitHub:

    .. code-block:: sh

        pip install https://github.com/barseghyanartur/django-debug-toolbar-force/archive/stable.tar.gz

    or latest stable version from BitBucket:

    .. code-block:: sh

        pip install https://bitbucket.org/barseghyanartur/django-debug-toolbar-force/get/stable.tar.gz

(2) Add ``debug_toolbar_force.middleware.ForceDebugToolbarMiddleware`` to
    ``MIDDLEWARE`` (or ``MIDDLEWARE_CLASSES`` for older versions of Django)
    of the your projects' Django settings (you would
    typically do that in your dev settings only).

    .. code-block:: python

        MIDDLEWARE += (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
            'debug_toolbar_force.middleware.ForceDebugToolbarMiddleware',
        )

Usage
=====
In your browser, visit a non-HTML view and append ``?debug-toolbar`` at the
end.

.. code-block:: text

    GET http://localhost:8000/foo/json-view/?debug-toolbar

Testing
=======
Simply type:

.. code-block:: sh

    ./runtests.py

or use tox:

.. code-block:: sh

    tox

or use tox to check specific env:

.. code-block:: sh

    tox -e py36

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
