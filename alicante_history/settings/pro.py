import os

from alicante_history.settings.base import *

DEBUG = True

BASE_URL = 'http://localhost:8000'
API_URL = ''

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ.get('ALICANTE_HISTORY_HOST_DB'),
            'PORT': os.environ['ALICANTE_HISTORY_PORT_DB'],
        }
    }
