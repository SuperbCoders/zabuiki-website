from .base import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['zabuiki.appspot.com', '127.0.0.1',]

STATIC_URL = os.environ['STATIC_URL']

MEDIA_URL = os.environ['MEDIA_URL']

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'zabuiki-static')

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'zabuiki-media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD']
    }
}

"""
'NAME': 'zabuiki-db',
'USER' : 'postgres',
'PASSWORD' : 'Et142teqIFwOxpaz',
"""