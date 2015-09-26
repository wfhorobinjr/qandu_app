"""
Django settings for qandu_app project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
ON_HEROKU = os.getenv('ON_HEROKU', False)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^t!a0_jbzalx-5&axnh8ob!of7fee-vnxzvzgx7m_pgl&3toli'

# SECURITY WARNING: don't run with debug turned on in production!
if ON_HEROKU == True:
  DEBUG = False
else:
  DEBUG = True

ALLOWED_HOSTS = []


    # Application definition

INSTALLED_APPS = (
      'registration',
      'django.contrib.sites',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'core',
      'bootstrap3',
    )
MIDDLEWARE_CLASSES = (
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
      'django.middleware.security.SecurityMiddleware',
    )
ROOT_URLCONF = 'qandu_app.urls'

TEMPLATES = [
      {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(MAIN_DIR, 'templates')],
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

WSGI_APPLICATION = 'qandu_app.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if ON_HEROKU == False:
      DATABASES = {
        'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
      }
else:
        DATABASES = {}
        import dj_database_url
        DATABASES['default'] =  dj_database_url.config()
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
        ALLOWED_HOSTS = ['*']


        # Internationalization
        # https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(MAIN_DIR, 'static'),)
STATIC_ROOT = 'staticfiles'
LOGIN_URL = '/user/login'
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1