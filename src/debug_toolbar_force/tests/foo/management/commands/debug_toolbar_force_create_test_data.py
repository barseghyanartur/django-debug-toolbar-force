from django.core.management.base import BaseCommand

from ....helpers import (
    get_or_create_admin_user,
    create_test_data
)

__all__ = ('Command',)


class Command(BaseCommand):
    """Creates test data."""

    def handle(self, *args, **options):
        """Handle."""
        try:
            user = get_or_create_admin_user()
            create_test_data(user)
        except Exception:
            pass
