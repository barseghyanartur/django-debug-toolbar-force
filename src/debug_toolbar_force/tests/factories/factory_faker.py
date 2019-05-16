# coding=utf-8

from __future__ import unicode_literals

from factory import Faker as OriginalFaker

__title__ = 'debug_toolbar_force.tests.factories.factory_faker'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2019 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'Faker',
)


class Faker(OriginalFaker):
    """Override to change the default locale."""

    _DEFAULT_LOCALE = 'nl_NL'
