"""
Django settings for tutorial project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import os.path as op

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
if 'HIGLASS_SERVER_BASE_DIR' in os.environ:
    base_dir = os.environ['HIGLASS_SERVER_BASE_DIR']

    if op.exists(base_dir):
        BASE_DIR = base_dir
    else:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e71$i%^qmf9cml7-ga@r+h3&v$y4c48a&u@%@$8t87z*qz9#ks'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['52.45.229.11', 'localhost', '127.0.0.1', 'higlass.site', 'higlass.io']

if 'SITE_URL' in os.environ:
    ALLOWED_HOSTS += [os.environ['SITE_URL']]

# this specifies where uploaded files will be place (e.g. BASE_DIR/media/uplaods/file.x)
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'log/hgs.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'WARNING',
        },
        'tilesets': {
            'handlers': ['file'],
            'level': 'WARNING',
        },
    }
}

if DEBUG:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']

if 'REDIS_HOST' in os.environ and 'REDIS_PORT' in os.environ:
    REDIS_HOST = os.environ['REDIS_HOST']
    REDIS_PORT = os.environ['REDIS_PORT']
else:
    REDIS_HOST = None
    REDIS_PORT = None

DEFAULT_FILE_STORAGE = 'tilesets.storage.HashedFilenameFileSystemStorage'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tilesets.apps.TilesetsConfig',
    'fragments.app.FragmentsConfig',
    'rest_framework_swagger',
    'corsheaders',
    'guardian'
]

# We want to avoid loading into memory
FILE_UPLOAD_HANDLERS = ['django.core.files.uploadhandler.TemporaryFileUploadHandler']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
    'guardian.backends.ObjectPermissionBackend',
)

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = False

CORS_ORIGIN_WHITELIST = (
    '134.174.140.208:9000'
)

# CORS_ALLOW_HEADERS = default_headers

ROOT_URLCONF = 'higlass_server.urls'

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

WSGI_APPLICATION = 'higlass_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

# STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
# )

#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
