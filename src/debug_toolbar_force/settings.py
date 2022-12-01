from .conf import get_setting

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2016-2022 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = (
    "GET_PARAM_NAME_FORCE",
    "GET_PARAM_NAME_NON_AJAX",
)

GET_PARAM_NAME_FORCE = get_setting("GET_PARAM_NAME_FORCE")
GET_PARAM_NAME_NON_AJAX = get_setting("GET_PARAM_NAME_NON_AJAX")
