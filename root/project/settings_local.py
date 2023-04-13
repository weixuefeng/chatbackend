# -*- coding: utf-8 -*-
"""
Django settings for project

"""
from config import codes
from config.server import *

# import common settings 

APPEND_SLASH = True

LOGGING_API_REQUEST = True

STATIC_DEFAULT_VERSION = 1

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    "django.core.context_processors.request",
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.csrf',
    'context_processors.settings_variable',
)

PAGE_SIZE = 50

CLIENT_APP_LANGUAGE = ['zh', 'en']

