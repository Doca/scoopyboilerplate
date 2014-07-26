"""
Django settings for a boilerplate project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
import sys


DEBUG = False
########### PROJECT DIRECTORY AND GENERAL SETTINGS
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))
SITE_ROOT = os.path.dirname(PROJECT_ROOT)
sys.path.append(PROJECT_ROOT)
SITE_NAME = os.path.basename(PROJECT_ROOT)
ROOT_URLCONF = '%s.urls' % SITE_NAME
########### END PROJECT DIRECTORY AND GENERAL SETTINGS


###########SECURITY
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['.*']

########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

LOCAL_APPS = (
    'compressor',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'static'))
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

TEMPLATE_LOADERS = (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


TIME_ZONE = 'Europe/Berlin'

LANGUAGE_CODE = 'de-de'

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

FIXTURE_DIRS = (
     os.path.join(PROJECT_ROOT, 'fixtures'),
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
COMMUNICATION_SENDER_MAIL = 'noreply@noreply.de'
DEFAULT_FROM_EMAIL = 'cantzen@googlemail.com'

CONTACT_MAIL = ['cantzen@googlemail.com']
DEFAULT_FROM_EMAIL = 'cantzen@googlemail.com'
SERVER_EMAIL = 'cantzen@googlemail.com  '
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cantzen@googlemail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PW']
