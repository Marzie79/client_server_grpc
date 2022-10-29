"""
Django settings for client project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6mr@-dq!+d81#*0xi%1cd72(&h#9cxh9rqi5pe2d90668i+u6y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'customer.apps.CustomerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_grpc',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'client.urls'

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

WSGI_APPLICATION = 'client.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

GRPC_SERVERS = {
    "SSO_HOST": os.environ.get("SSO_GRPC_SERVER_HOST", 'localhost'),
    "SSO_PORT": os.environ.get("SSO_GRPC_SERVER_PORT", 50151),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = 'amqp://username:password@127.0.0.2'
CELERY_TIMEZONE = TIME_ZONE
CELERY_RESULT_BACKEND = "rpc://"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

STREAM_INFO = {
    'SERVER_SERVICE_EXCHANGE': os.environ.get(
        'SERVER_SERVICE_EXCHANGE', "server"
    ),
    'SERVER_SERVICE_DEFAULT_ROUTING_KEY': os.environ.get(
        'SERVER_SERVICE_DEFAULT_ROUTING_KEY', 'server'
    ),
    'CLIENT_SERVICE_LOG_ROUTING_KEY': os.environ.get(
        'CLIENT_SERVICE_LOG_ROUTING_KEY',
        'client.log_routing'
    ),
    'CLIENT_SERVICE_EXCHANGE': os.environ.get(
        'CLIENT_SERVICE_EXCHANGE', 'client.test'
    ),
    'CLIENT_SERVICE_SEND_LOG_ROUTING_KEY': os.environ.get(
        'CLIENT_SERVICE_SEND_LOG_ROUTING_KEY',
        'client.client_routing'
    ),
    'CLIENT_SERVICE_SEND_LOG_QUEUE': os.environ.get(
        'CLIENT_SERVICE_SEND_LOG_QUEUE',
        'client.send_log_queue'
    )
}
