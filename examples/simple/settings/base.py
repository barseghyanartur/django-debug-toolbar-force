# Django settings for example project.
import os
import sys

from django_nine import versions

from .core import PROJECT_DIR, gettext, show_toolbar


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False
DEBUG_TOOLBAR = False
DEV = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': PROJECT_DIR(os.path.join('..', '..', 'db', 'example.db')),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', gettext("English")),  # Main language!
    ('hy', gettext("Armenian")),
    ('nl', gettext("Dutch")),
    ('ru', gettext("Russian")),
    ('de', gettext("German")),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR(os.path.join('..', '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_DIR(os.path.join('..', '..', 'static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR(os.path.join('..', '..', 'media', 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '97818c*w97Zi8a-m^1coRRrmurMI6+q5_kyn*)s@(*_Pk6q423'

try:
    from .local_settings import DEBUG_TEMPLATE
except Exception as err:
    DEBUG_TEMPLATE = False

if versions.DJANGO_GTE_1_10:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # 'APP_DIRS': True,
            'DIRS': [PROJECT_DIR(os.path.join('..', 'templates'))],
            'OPTIONS': {
                'context_processors': [
                    "django.template.context_processors.debug",
                    'django.template.context_processors.request',
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    # "context_processors.testing",  # Testing
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    # 'django.template.loaders.eggs.Loader',
                ],
                'debug': DEBUG_TEMPLATE,
            }
        },
    ]
elif versions.DJANGO_GTE_1_8:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # 'APP_DIRS': True,
            'DIRS': [PROJECT_DIR(os.path.join('..', 'templates'))],
            'OPTIONS': {
                'context_processors': [
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.request",
                    # "context_processors.testing",  # Testing
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'django.template.loaders.eggs.Loader',
                ],
                'debug': DEBUG_TEMPLATE,
            }
        },
    ]
else:
    TEMPLATE_DEBUG = DEBUG_TEMPLATE

    # List of callables that know how to import templates from various
    # sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
    )

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or
        # "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        PROJECT_DIR(os.path.join('..', 'templates')),
    )

if versions.DJANGO_GTE_1_10:
    MIDDLEWARE = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
else:
    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

# FIXTURE_DIRS = (
#   PROJECT_DIR(os.path.join('..', 'fixtures'))
# )

INSTALLED_APPS = [
    # Django core and contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',

    # Other project specific apps
    # 'debug_toolbar_force',  # Test app
    'debug_toolbar_force.tests.foo',  # Test app
]

LOGIN_URL = '/en/accounts/login/'
LOGIN_ERROR_URL = '/en/accounts/login/'
LOGOUT_URL = '/en/accounts/logout/'
LOGIN_REDIRECT_URL = '/en/'

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
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        "": {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'debug_toolbar_force': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
