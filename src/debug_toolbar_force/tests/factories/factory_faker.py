# coding=utf-8

from __future__ import unicode_literals

from factory import Faker as OriginalFaker

__title__ = 'debug_toolbar_force.tests.factories.factory_faker'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'Faker',
)


class Faker(OriginalFaker):
    """Override to change the default locale."""

    _DEFAULT_LOCALE = 'nl_NL'
