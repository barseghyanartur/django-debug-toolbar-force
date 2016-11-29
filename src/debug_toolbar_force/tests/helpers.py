from django.core.management import call_command

from .base import (
    is_app_setup_completed,
    mark_app_setup_as_completed
)

from .factories import (
    SiteFactory,
    SuperAdminUserFactory,
    UserFactory
)

__title__ = 'debug_toolbar_force.tests.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'setup_app',
    'get_or_create_admin_user',
    'create_test_data',
)


def setup_app(collectstatic=False, migrate=False):
    """Set up."""
    if is_app_setup_completed():
        return False

    if collectstatic:
        call_command('collectstatic', verbosity=3, interactive=False)

    if migrate:
        call_command('migrate', verbosity=3, interactive=False)

    mark_app_setup_as_completed()


def get_or_create_admin_user():
    """Get or create admin user."""
    return SuperAdminUserFactory()


def create_test_data(user=None):
    """Create test data."""
    SiteFactory()
    UserFactory.create_batch(size=10)
