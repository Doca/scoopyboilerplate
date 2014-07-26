from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

COMPRESS = True
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

COMPRESS_CSS_FILTERS = ('compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.CSSMinFilter',)


TEMPLATE_LOADERS = (
    (
        'django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )
    ),
)

PREPEND_WWW = True

ADMINS = (
    ('Dorian Cantzen', 'cantzen@extrument.com'),
)



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}