import json

from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from nine.versions import DJANGO_GTE_1_10
from six import text_type

from .settings import GET_PARAM_NAME_FORCE, GET_PARAM_NAME_NON_AJAX

__title__ = 'debug_toolbar_force.middleware'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ForceDebugToolbarMiddleware',)


class ForceDebugToolbarMiddleware(object):
    """The `django-debug-toolbar` for views that do not return HTML."""

    if DJANGO_GTE_1_10:
        def __init__(self, get_response=None):
            self.get_response = get_response
            super(ForceDebugToolbarMiddleware, self).__init__()

        def __call__(self, request):
            response = None
            if hasattr(self, 'process_request'):
                response = self.process_request(request)
            if not response:
                response = self.get_response(request)
            if hasattr(self, 'process_response'):
                response = self.process_response(request, response)
            return response

    def process_request(self, request):
        """Process request.

        If `GET_PARAM_NAME_NON_AJAX` is present in request.GET, set
        request.is_ajax to False.
        """
        non_ajax = True if GET_PARAM_NAME_NON_AJAX in request.GET else False
        if non_ajax:
            request.is_ajax = False
        return None

    def process_response(self, request, response):
        """Process response.

        If `GET_PARAM_NAME_FORCE` is present in request.GET wrap response
        in <html><body>{{ response }}</body></html>.
        """
        debug = True if GET_PARAM_NAME_FORCE in request.GET else False

        if debug:
            if response['Content-Type'] == 'application/octet-stream':
                new_content = '<html><body>' \
                              '{}: {}</body></html>' \
                              ''.format(_("Binary Data, Length"),
                                        len(response.content))
                response = HttpResponse(new_content)
            elif response['Content-Type'] != 'text/html':
                content = response.content
                try:
                    json_ = json.loads(text_type(content))
                    content = json.dumps(json_, sort_keys=True, indent=2)
                except ValueError:
                    pass
                response = HttpResponse('<html><body>{}'
                                        '</body></html>'.format(content))

        return response
