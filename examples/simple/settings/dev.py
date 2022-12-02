from .base import *

# Do not put any settings below this line
try:
    from .local_settings import *
except:
    pass

if DEBUG and DEBUG_TOOLBAR:
    try:
        # Make sure the django-debug-toolbar is installed
        import debug_toolbar

        # debug_toolbar

        MIDDLEWARE += (
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
