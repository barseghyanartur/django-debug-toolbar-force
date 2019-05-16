from factory import DjangoModelFactory

from django.conf import settings
from django.contrib.sites.models import Site

from .factory_faker import Faker

__title__ = 'debug_toolbar_force.tests.factories.sites_site'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2019 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'SiteFactory',
    'DefaultSiteFactory',
)


class SiteFactory(DjangoModelFactory):
    """Factory for creating a site."""

    domain = Faker('domain_name')
    name = Faker('domain_name')

    class Meta(object):
        """Meta."""

        model = Site


class DefaultSiteFactory(SiteFactory):
    """Factory for creating a default site."""

    id = settings.SITE_ID

    class Meta(object):
        """Meta class."""

        model = Site
        django_get_or_create = ('id',)
