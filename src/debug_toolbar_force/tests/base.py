from __future__ import print_function

import logging

__title__ = 'debug_toolbar_force.tests.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2019 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'app_setup',
    'is_app_setup_completed',
    'LOG_INFO',
    'log_info',
    'mark_app_setup_as_completed',
    'skip',
)


LOGGER = logging.getLogger(__name__)

LOG_INFO = True


def log_info(func):
    """Log some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        """Inner."""
        result = func(self, *args, **kwargs)

        LOGGER.info('\n%s', func.__name__)
        LOGGER.info('============================')
        if func.__doc__:
            LOGGER.info('""" %s """', func.__doc__.strip())
        LOGGER.info('----------------------------')
        if result is not None:
            LOGGER.info(result)
        LOGGER.info('\n')

        return result
    return inner


SKIP = False


def skip(func):
    """Simply skip the test."""
    def inner(self, *args, **kwargs):
        """Inner."""
        if SKIP:
            return
        return func(self, *args, **kwargs)
    return inner


class AppSetup(object):
    """Basic setup class.

    Created in order to avoid the app test data to be initialised
    multiple times.
    """
    def __init__(self):
        self.is_done = False


app_setup = AppSetup()


def is_app_setup_completed():
    """Check if app setup is completed."""
    return app_setup.is_done is True


def mark_app_setup_as_completed():
    """Mark app setup as completed."""
    app_setup.is_done = True
