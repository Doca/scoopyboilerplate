from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

COMPRESS = True
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

COMPRESS_CSS_FILTERS = ('compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.CSSMinFilter',)

COMPRESS_CLOSURE_COMPILER_BINARY = '/usr/local/bin/closure'
COMPRESS_CLOSURE_COMPILER_ARGUMENTS = '--language_in=ECMASCRIPT5'
COMPRESS_JS_FILTERS = ('compressor.filters.closure.ClosureCompilerFilter',)

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