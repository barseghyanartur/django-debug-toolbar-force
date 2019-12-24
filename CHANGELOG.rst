Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.1.7
-----
2019-12-24

- Added Django 3.0 support.
- Tested against Python 3.8.

0.1.6
-----
2019-09-24

- Minor fixes and tests improvements.

0.1.5
-----
2019-04-12

- Tested against Django 2.1 and 2.2.
- Drop Python 3.4 support.
- Tested against Python 3.7.

0.1.4
-----
2018-07-02

- Minor compatibility fixes.

0.1.3
-----
2017-12-30

- Django 2.0 support.

0.1.2
-----
2017-04-14

- Django 1.11 support.

0.1.1
-----
2016-12-21

- Minor fixes.

0.1
---
2016-11-29

- Initial release.
