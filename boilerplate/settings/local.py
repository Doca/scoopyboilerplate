from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

COMPRESS = True
INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'testproject',
        'PASSWORD': os.environ['DATABASE_PW'],
        'USER':'root'
    }
}

INSTALLED_APPS += ('debug_toolbar',
                   )