from django.conf.urls import url

from .views import (
    ajax_view,
    html_view,
    json_bytes_view,
    json_view,
    partial_html_view,
)

__title__ = 'debug_toolbar_force.tests.foo.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2019 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('urlpatterns',)


urlpatterns = [
    url(r'^ajax-view/$', view=ajax_view, name='foo.ajax_view'),
    url(r'^json-view/$', view=json_view, name='foo.json_view'),
    url(r'^json-bytes-view/$',
        view=json_bytes_view,
        name='foo.json_bytes_view'),
    url(r'^html-view/$', view=html_view, name='foo.html_view'),
    url(r'^partial-html-view/$',
        view=partial_html_view,
        name='foo.partial_html_view'),
]
