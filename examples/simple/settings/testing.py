from .base import *

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

INTERNAL_IPS = (
    "127.0.0.1",
    "*",
)

DEBUG = True
DEBUG_TOOLBAR = True
DEBUG_TEMPLATE = True
DEV = True
DEBUG_TOOLBAR_FORCE_GET_PARAM_NAME_FORCE = "debug-toolbar"

if DEBUG and DEBUG_TOOLBAR:
    try:
        # Make sure the django-debug-toolbar is installed
        import debug_toolbar

        # debug_toolbar
        if versions.DJANGO_GTE_1_10:
            MIDDLEWARE += (
                "debug_toolbar.middleware.DebugToolbarMiddleware",
                "debug_toolbar_force.middleware.ForceDebugToolbarMiddleware",
            )
        else:
            MIDDLEWARE_CLASSES += (
                "debug_toolbar.middleware.DebugToolbarMiddleware",
                "debug_toolbar_force.middleware.ForceDebugToolbarMiddleware",
            )

        INSTALLED_APPS += ("debug_toolbar",)

        DEBUG_TOOLBAR_CONFIG = {
            "INTERCEPT_REDIRECTS": False,
            "SHOW_TOOLBAR_CALLBACK": "settings.base.show_toolbar",
        }
    except ImportError:
        pass

# Make the `django-debug-toolbar-force` package available without
# installation.
if DEV:
    debug_toolbar_force_source_path = os.environ.get(
        "DEBUG_TOOLBAR_FORCE_SOURCE_PATH", "src"
    )
    sys.path.insert(0, os.path.abspath(debug_toolbar_force_source_path))
