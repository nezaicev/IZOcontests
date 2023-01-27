"""
Django settings for cnho project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import logging
import os

from pathlib import Path
from environs import Env
from dotenv import load_dotenv
from celery.schedules import crontab

load_dotenv()
env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", True)

ALLOWED_HOSTS = ['*']
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000
# Application definition

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'mailing.apps.MailingConfig',
    'contests.apps.ContestsConfig',
    'map.apps.MapConfig',
    'cert.apps.CertConfig',
    'event.apps.EventConfig',
    'exposition.apps.ExpositionConfig',
    'content.apps.ContentConfig',
    'ckeditor',
    'ckeditor_uploader',
    'multiselectfield',
    'frontend',
    'rest_framework',
    'corsheaders',
    'sorl.thumbnail',
    'django_static_fontawesome',
    'django_changelist_toolbar_admin',
    'django_simple_export_admin',
    'phonenumber_field'

]

# CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'cnho.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'cnho.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', ''),
    },
    'vm': {
        'ENGINE': os.getenv('MODX_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('MODX_DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('MODX_DB_USER', ''),
        'PASSWORD': os.getenv('MODX_DB_PASSWORD', ''),
        'HOST': os.getenv('MODX_DB_HOST', ''),
        'PORT': os.getenv('MODX_DB_PORT', ''),
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'users.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = os.getenv('STATIC_URL', '/static/')
STATICFILES_DIRS = [
    os.getenv('STATICFILES_DIRS', os.path.join(BASE_DIR, 'static')),
    os.getenv('STATICFILES_DIRS', os.path.join(BASE_DIR, 'frontend')),
]

# STATIC_ROOT=os.getenv('STATIC_ROOT',os.path.join(BASE_DIR,'static'))

PATH_IMG_UPLOAD = 'all_contests/'
TMP_DIR = os.path.join(BASE_DIR, 'media', 'tmp')

MEDIA_URL = os.getenv('MEDIA_URL', '/media/')
MEDIA_ROOT = os.getenv('MRDIA_ROOT', os.path.join(BASE_DIR, 'media'))
BARCODE_MEDIA_ROOT = os.getenv('BARCODE_URL',
                               os.path.join(BASE_DIR, 'media/barcode/'))

FILE_UPLOAD_MAX_MEMORY_SIZE = 20621440

LOGIN_REDIRECT_URL = 'home_frontend'
LOGOUT_REDIRECT_URL = 'home_frontend'

EMAIL_BACKEND = os.getenv("EMAIL_BACKEND",
                          "django.core.mail.backends.filebased.EmailBackend")
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_PORT = os.getenv("EMAIL_PORT", 587)
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_FROM', 'webmaster@localhost')
EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))

EMAIL_CONTEST = {
    'host': os.getenv('EMAIL_HOST'),
    'from_contest': os.getenv('EMAIL_FROM'),
    'port': 587,
    'use_tls': True
}

SELECTEL_STORAGES = {
    'default': {
        'USERNAME': os.getenv("USERNAME_SELECTEL"),
        'PASSWORD': os.getenv("PASSWORD_SELECTEL"),
        'CONTAINER': os.getenv("CONTAINER_SELECTEL"),
    },

}
PROTOCOL = 'http://'

YOUTUBE_POSTER = 'https://img.youtube.com/vi/{}/mqdefault.jpg'
POSTER_DIR = 'posters'
POSTER_TMP_NAME = 'tmp_poster.jpg'

DEFAULT_FILE_STORAGE = 'django_selectel_storage.storage.SelectelStorage'

CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_UPLOAD_PATH = os.getenv("CE_UPLOAD_PATH", "uploads/")
# CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
CKEDITOR_CONFIGS = {
    'default': {
        'allowedContent': True,
        'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document',
             'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print',
                       '-', 'Templates']},
            {'name': 'clipboard',
             'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
                       '-', 'Undo', 'Redo']},
            {'name': 'editing',
             'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea',
                       'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                       'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent',
                       'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight',
                       'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley',
                       'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles',
             'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'image2',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}

REST_FRAMEWORK = {

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,

}
