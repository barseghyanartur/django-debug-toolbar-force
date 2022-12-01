from django.urls import re_path

from .views import (
    ajax_view,
    html_view,
    json_bytes_view,
    json_view,
    partial_html_view,
)

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2016-2022 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("urlpatterns",)


urlpatterns = [
    re_path(r"^ajax-view/$", view=ajax_view, name="foo.ajax_view"),
    re_path(r"^json-view/$", view=json_view, name="foo.json_view"),
    re_path(
        r"^json-bytes-view/$", view=json_bytes_view, name="foo.json_bytes_view"
    ),
    re_path(r"^html-view/$", view=html_view, name="foo.html_view"),
    re_path(
        r"^partial-html-view/$",
        view=partial_html_view,
        name="foo.partial_html_view",
    ),
]
