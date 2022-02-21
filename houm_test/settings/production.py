import os
from datetime import timedelta
from houm_test.core_settings import *

DEBUG = False
ADMIN_ENABLED = False

ALLOWED_HOSTS = ['.host.com', 'IP']

# Database
DATABASES = {
    'default': {
        'ENGINE': os.getenv("DB_ENGINE"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT")
    }
}


# BOILERPLATE Modify the app base url to allow calls from the Local webapp
CORS_ORIGIN_REGEX_WHITELIST = (
    r'^https://host.com$',
)

SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(hours=1)
