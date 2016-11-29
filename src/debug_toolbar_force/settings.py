from .conf import get_setting

__title__ = 'debug_toolbar_force.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'GET_PARAM_NAME_FORCE',
    'GET_PARAM_NAME_NON_AJAX',
)

GET_PARAM_NAME_FORCE = get_setting('GET_PARAM_NAME_FORCE')
GET_PARAM_NAME_NON_AJAX = get_setting('GET_PARAM_NAME_NON_AJAX')
