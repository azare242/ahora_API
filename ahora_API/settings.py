"""
Django settings for ahora_API project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y^ffvp!y#r6b44j!52%jw0g^faio&2rhh*w71s6l#38_=wi$g^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL =  os.path.join(BASE_DIR, 'staticfiles/web/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/web/media/')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 'boys',
    'RequestsService'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.json.JSONMiddleware',
    
]

ROOT_URLCONF = 'ahora_API.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ahora_API.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTH_USER_MODEL = 'RequestsService.CustomUser'

HASHID_FIELD_SALT = '$oknhgfcv$!#$!@$mkloiuy8767$#!$@#8490398!#@$!'  # Replace with your secret salt
HASHID_FIELD_ALLOW_INT_LOOKUP = True  # Allow looking up by integer value


#Celery
CELERY_BROKER_URL = \
'amqps://fhisssit:L49-h0zwCZ5D4SKkQm9I25NMhfriMf0G@chimpanzee.rmq.cloudamqp.com/fhisssit'


#S3
S3_ENDPOINT = 'https://cloudhw-ahora.s3.ir-tbz-sh1.arvanstorage.ir'
S3_ACCESS_KEY = '7af1a7fd-876b-41e6-ba85-d070c78e8c9c'
S3_SECRET_KEY = 'efa744fce877e3d4d064a5a830a97f93fe94576b92100530e0ad2c676eb0dfe0'



#IMAGGA
IMAGGA_API_KEY = 'acc_5f1444fe4d81570'
IMAGGA_SECRET_KEY = '4615a8b7d71cbe2048a9803566b857c3'
IMAGGA_AUTH = 'Basic YWNjXzVmMTQ0NGZlNGQ4MTU3MDo0NjE1YThiN2Q3MWNiZTIwNDhhOTgwMzU2NmI4NTdjMw=='

