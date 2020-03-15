import os
from django.utils.translation import ugettext_lazy as _

from .utils import read_secret


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = os.environ.get('ENV') == 'DEV'
PROD = os.environ.get('ENV') == 'PROD'

STATIC_URL = '/assets/'
STATIC_ROOT = '/src/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = '/data/files/media/'
MEDIA_URL = '/media/'
ROOT_URLCONF = 'core.urls'

SECRET_KEY = read_secret('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = [os.environ.get('HOST_NAME'), os.environ.get('SERVER_IP')]
BASE_URL = os.environ.get('HOST_NAME')

# Email related settings
ADMINS = [('IT Team', os.environ['ADMIN_EMAIL'])]
EMAIL_BACKEND = 'mailer.backend.DbBackend'
MAILER_EMAIL_BACKEND = 'core.rewrite_email_backend.EmailBackend'
SERVER_EMAIL = os.environ['SERVER_EMAIL']
EMAIL_SUBJECT_PREFIX = '[%s] ' % os.environ.get('HOST_NAME')
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = int(os.environ['EMAIL_PORT'])
EMAIL_HOST_USER = read_secret('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = read_secret('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
MAILER_LOCK_PATH = '/tmp/mailer_lock'
ADMIN_EMAIL = os.environ['ADMIN_EMAIL']

INSTALLED_APPS = [
    # django core packages -> Load them before anything else
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party packages -> Load them before the our packages are loaded
    'django_extensions',
    'mailer',
    'channels',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django_filters',
    'easy_thumbnails',

    # gStack packages
    'core',
    'myuser',

    # django core packages -> Load them here so we can override them
    'django.contrib.admin',

    # 3rd party packages -> Load them last so we can override them
    'explorer',
    'rosetta'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda x: DEBUG
    }

pwd_path = 'django.contrib.auth.password_validation.'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': pwd_path + 'MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': pwd_path + 'UserAttributeSimilarityValidator',
        'OPTIONS': {
            'user_attributes': ('first_name', 'last_name', 'email'),
        }
    },
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = "core.routing.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}

# Set up custom user model
AUTH_USER_MODEL = 'myuser.User'

# Database
db_password = read_secret('DB_PASSWORD')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'postgres',
        'PORT': '5432',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': db_password,
    },
    'explorer': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'postgres',
        'PORT': '5432',
        'NAME': 'django',
        'USER': 'explorer',
        'PASSWORD': db_password,
        'TEST': {
            'MIRROR': 'default',
        }
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # Use this if you want to disable the form on the BrowsableAPIRenderer
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'core.renderers.BrowsableAPIRendererWithoutForm',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination'
    ),
    'PAGE_SIZE': 10,
    'MAX_PAGE_SIZE': 1000,
    'PAGINATE_BY_PARAM': 'page_size'
}


EXPLORER_DEFAULT_CONNECTION = 'explorer'
EXPLORER_CONNECTIONS = {'Default': 'explorer'}
EXPLORER_DATA_EXPORTERS = [
    ('csv', 'core.exporters.CSVExporterBOM'),
    ('excel', 'explorer.exporters.ExcelExporter'),
    ('json', 'explorer.exporters.JSONExporter')
]

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('hu', _('Hungarian')),
)

LOCALE_PATHS = ('/data/files/locale/',)
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# ROSETTA
ROSETTA_MESSAGES_PER_PAGE = 50
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

DATE_FORMAT = ('Y-m-d')
DATETIME_FORMAT = ('Y-m-d H:i:s')
TIME_FORMAT = ('H:i:s')

# File Upload max 50MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o750
FILE_UPLOAD_PERMISSIONS = 0o640

# Set up custom user model
# AUTH_USER_MODEL =

# After a successful authentication this is where we go
# LOGIN_REDIRECT_URL =

# The login page is also the start page too
LOGIN_URL = '/admin/'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
