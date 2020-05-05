from .base import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, '../zabuiki-be368f3e9c0a.json')

DEFAULT_FILE_STORAGE = 'zabuiki.settings.gcloud.GoogleCloudMediaFileStorage'
STATICFILES_STORAGE = 'zabuiki.settings.gcloud.GoogleCloudStaticFileStorage'
    
GS_PROJECT_ID = 'zabuiki'
GS_STATIC_BUCKET_NAME = 'zabuiki-statics'
GS_MEDIA_BUCKET_NAME = 'zabuiki-media'
    
STATIC_URL = 'https://storage.googleapis.com/{}/'.format(GS_STATIC_BUCKET_NAME)
STATIC_ROOT = "static/"

MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_MEDIA_BUCKET_NAME)
MEDIA_ROOT = "media/"
    
UPLOAD_ROOT = 'media/uploads/'
    
DOWNLOAD_ROOT = os.path.join(BASE_DIR, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../frontend/static'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
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