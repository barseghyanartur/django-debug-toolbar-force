from .base import *

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['all_log'],
    },
    'formatters': {
        'verbose': {
            'format': '\n%(levelname)s %(asctime)s [%(pathname)s:%(lineno)s] '
                      '%(message)s'
        },
        'simple': {
            'format': '\n%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'all_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/all.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'django_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/django.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'django_request_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/django_request.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'debug_toolbar_force_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/debug_toolbar_force.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['django_request_log'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['django_log'],
            'level': 'ERROR',
            'propagate': False,
        },
        'debug_toolbar_force': {
            'handlers': ['console', 'debug_toolbar_force_log'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

INTERNAL_IPS = ('127.0.0.1', '*',)

DEBUG = True
DEBUG_TOOLBAR = True
DEBUG_TEMPLATE = True
DEV = True

if DEBUG and DEBUG_TOOLBAR:
    try:
        # Make sure the django-debug-toolbar is installed
        import debug_toolbar

        # debug_toolbar
        if versions.DJANGO_GTE_1_10:
            MIDDLEWARE += (
                'debug_toolbar.middleware.DebugToolbarMiddleware',
                'debug_toolbar_force.middleware.ForceDebugToolbarMiddleware',
            )
        else:
            MIDDLEWARE_CLASSES += (
                'debug_toolbar.middleware.DebugToolbarMiddleware',
                'debug_toolbar_force.middleware.ForceDebugToolbarMiddleware',
            )

        INSTALLED_APPS += (
            'debug_toolbar',
        )

        DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
            'SHOW_TOOLBAR_CALLBACK': 'settings.base.show_toolbar'
        }
    except ImportError:
        pass

# Make the `django-debug-toolbar-force` package available without
# installation.
if DEV:
    debug_toolbar_force_source_path = os.environ.get(
        'DEBUG_TOOLBAR_FORCE_SOURCE_PATH',
        'src'
    )
    sys.path.insert(0, os.path.abspath(debug_toolbar_force_source_path))
