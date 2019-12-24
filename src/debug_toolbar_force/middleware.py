from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _

from nine.versions import DJANGO_GTE_1_10


from .settings import GET_PARAM_NAME_FORCE, GET_PARAM_NAME_NON_AJAX

__title__ = 'debug_toolbar_force.middleware'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016-2019 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
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
        non_ajax = GET_PARAM_NAME_NON_AJAX in request.GET
        if non_ajax:
            request.is_ajax = False
        return None

    def process_response(self, request, response):
        """Process response.

        If `GET_PARAM_NAME_FORCE` is present in request.GET wrap response
        in <html><body>{{ response }}</body></html>.
        """
        debug = GET_PARAM_NAME_FORCE in request.GET

        if debug:
            if response['Content-Type'] == 'application/octet-stream':
                new_content = '<html><body>' \
                              '{}: {}</body></html>' \
                              ''.format(_("Binary Data, Length"),
                                        len(response.content))
                response = HttpResponse(new_content)
            elif response['Content-Type'] != 'text/html':
                content = smart_str(response.content)
                response = HttpResponse(u'<html><body>{}'
                                        u'</body></html>'.format(content))

        return response
