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
