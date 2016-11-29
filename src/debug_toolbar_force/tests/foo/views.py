from django.http import JsonResponse
from django.shortcuts import render

from six import text_type

__title__ = 'debug_toolbar_force.tests.foo.views'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'ajax_view',
    'json_view',
    'html_view',
    'partial_html_view',
)


def json_view(request):
    """JSON view."""
    return JsonResponse(text_type([1, 2, 3]), safe=False)


def ajax_view(request, template_name='foo/ajax_view.html'):
    """AJAX view."""
    return render(request, template_name, {'data': [1, 2, 3]})


def partial_html_view(request, template_name='foo/partial_html_view.html'):
    """Partial HTML view."""
    return render(request, template_name, {'data': [1, 2, 3]})


def html_view(request, template_name='foo/html_view.html'):
    """HTML view."""
    return render(request, template_name, {'data': [1, 2, 3]})
