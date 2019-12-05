import os

from alicante_history.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['165.22.69.202']

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('ALICANTE_HISTORY_NAME_DB'),
        'USER': os.environ.get('ALICANTE_HISTORY_USER_DB'),
        'PASSWORD': os.environ.get('ALICANTE_HISTORY_PASS_DB'),
        'HOST': os.environ.get('ALICANTE_HISTORY_HOST_DB'),
        'PORT': os.environ.get('ALICANTE_HISTORY_PORT_DB'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'images')
