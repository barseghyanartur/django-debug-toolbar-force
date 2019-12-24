import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


__title__ = 'debug_toolbar_force.tests.foo.views'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2019 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'ajax_view',
    'html_view',
    'json_bytes_view',
    'json_view',
    'partial_html_view',
)


def json_view(request):
    """JSON view."""
    # Standard Django way, content will be unicode
    return JsonResponse([1, 2, 3], safe=False)


def json_bytes_view(request):
    """JSON view, returns bytes"""
    # Something an application may do is return bytes instead of unicode
    return HttpResponse(json.dumps([1, 2, 3]), content_type="application/json")


def ajax_view(request, template_name='foo/ajax_view.html'):
    """AJAX view."""
    return render(request, template_name, {'data': [1, 2, 3]})


def partial_html_view(request, template_name='foo/partial_html_view.html'):
    """Partial HTML view."""
    return render(request, template_name, {'data': [1, 2, 3]})


def html_view(request, template_name='foo/html_view.html'):
    """HTML view."""
    return render(request, template_name, {'data': [1, 2, 3]})
