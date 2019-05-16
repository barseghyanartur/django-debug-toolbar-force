from django.apps import AppConfig

__title__ = 'debug_toolbar_force.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2019 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'debug_toolbar_force'
    label = 'debug_toolbar_force'
