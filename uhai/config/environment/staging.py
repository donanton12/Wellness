from uhai.config.settings import *
import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..','..'))
PARENT_HOST   = 'uhai.synacor.co.ke'

DJANGO_SETTINGS_MODULE = 'uhai.config.environment.staging'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += [
    'kombu.transport.django',     
    'djcelery',  
]

BROKER_URL = "django://" # tell kombu to use the Django database as the message queue  

MIDDLEWARE_CLASSES += [
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'uhai', 
        'HOST': 'localhost', 
        'USER': 'uhai', 
        'PASSWORD': 'e3e37cae', 
        'PORT': ''
    }
}

# e-mail settings
DEFAULT_FROM_EMAIL = 'noreply@uhai.com'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'uhai'
EMAIL_HOST_PASSWORD = 'a79fHH7722!'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', 
#         'NAME': '/home/uhai/webapp_releases/uhai/shared/database/uhai.db', 
#         'HOST': '', 
#         'USER': '', 
#         'PASSWORD': '', 
#         'PORT': ''
#     }
# }

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH,'templates'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH,'locale'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH,'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'static'),
)
