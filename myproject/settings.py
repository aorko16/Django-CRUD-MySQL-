import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-change-me-in-production'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'employees',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': ['django.template.context_processors.request']},
}]

WSGI_APPLICATION = 'myproject.wsgi.application'




DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.mysql',
       'NAME': os.environ.get('MYSQL_DB', 'devops'),
       'USER': os.environ.get('MYSQL_USER', 'admin'),
      'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'admin'),
      'HOST': os.environ.get('MYSQL_HOST', 'mysql'),
      'PORT': '3306',
  }
}


#DATABASES = {
#    'default': {
#       'ENGINE': 'django.db.backends.mysql',
#        'NAME': os.environ.get('MYSQL_DB', 'devops'),
#        'USER': os.environ.get('MYSQL_USER', 'admin'),
#       'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'admin'),
#       'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
#       'PORT': '3306',
#   }
#}






LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
