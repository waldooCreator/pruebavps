import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Settings allow easy overrides via environment variables for Docker
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'replace-this-with-a-secure-key-for-production')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'calc',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'webcalc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
            ],
        },
    },
]

WSGI_APPLICATION = 'webcalc.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'calc', 'static')]
# Folder where `collectstatic` will place files in production
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Use WhiteNoise to serve static files when running under Gunicorn
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
