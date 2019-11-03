import os

from alicante_history.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('ALICANTE_HISTORY_NAME_DB'),
        'USER': os.environ.get('ALICANTE_HISTORY_USER_DB'),
        'PASSWORD': os.environ.get('ALICANTE_HISTORY_PASS_DB'),
        'HOST': 'localhost',
        'PORT': ''                 # set to empty string for default
    }
}
