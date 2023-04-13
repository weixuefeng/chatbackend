# -*- coding: utf-8 -*-
__author__ = 'weixuefeng1018@gmail.com'
__version__ = '$Rev$'
__doc__ = """  """

import platform
from logging.handlers import SysLogHandler
from config import codes

SITE_ID = '1'
BASE_URL = 'http://127.0.0.1:8000'

ENV_DEV = True

# Media
MEDIA_URL = 'http://127.0.0.1:8000/filestorage/'
MEDIA_ROOT = '/Users/root/filestorage/'

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = 'root/static'


# DEBUG = True
DEBUG = True
TEMPLATE_DEBUG = False
THUMBNAIL_DEBUG = False
DOMAIN = '127.0.0.1'

# Cache
DEFAULT_CACHE_DB = 0
REDIS_CACHE_DB = DEFAULT_CACHE_DB
REDIS_CACHE_PASSWORD = ''
REDIS_CACHE_HOST = '127.0.0.1'
REDIS_CACHE_PORT = 6379
REDIS_CACHE_URL = 'redis://%s:%s' % (REDIS_CACHE_HOST, REDIS_CACHE_PORT)

WORKER_CACHE_DB = 0
REDIS_WORKER_URL = 'redis://127.0.0.1:6379'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "%s/%s" % (REDIS_CACHE_URL, DEFAULT_CACHE_DB),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'chat',
#         'USER': 'user1',
#         'PASSWORD': 'user1',
#         'HOST': '127.0.0.1',
#         'OPTIONS': {'charset': 'utf8mb4'},
#     },
# }

# 设置数据库的路由规则方法
DATABASE_ROUTERS = ['utils.database_router.DatabaseAppsRouter']
# 设置APP对应的数据库路由表，哪个app要连接哪个数据库，没有指定会用default那个。
DATABASE_APPS_MAPPING = {
    'admin': 'admin',
    'email_log': 'default',
    'admin': 'default',
    'django_extensions': 'default',
    'werkzeug_debugger_runserver': 'default',
    'staticfiles': 'default',
    'messages': 'default',
    'sessions': 'default',
    'contenttypes': 'default',
    'auth': 'default',

    'wallet': 'default',
    'nft': 'default',
    'common': 'default',
    'comment': 'default',
    'system': 'default',
    'channel': 'default',
    'order': 'default',
    'user': 'default',
    'api': 'default',
    'newton': 'default',
    'message': 'default',
    'banner': 'default',
    'activity': 'default',
    'evt': 'default',
    'event': 'default',
    'coffer': 'coffer',
}



# Email settings
EMAIL_DEBUG = True # True: don't send email, False: send email
# EMAIL BACKEND SETTING
EMAIL_BACKEND = 'email_log.backends.EmailBackend'
FROM_EMAIL = 'WaveMall<****@163.com>'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = '18735404398@163.com'
EMAIL_HOST_PASSWORD = '*****'
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
# EMAIL POOL SETTINGS
EMAIL_CODE_KEY_PREFIX = 'email_code_'
EMAIL_CODE_POOL = 'email_code_pool'
EMAIL_CODE_POOL_OPEN = True
EMAIL_CODE_TIMEOUT = 60 * 30
# SMS SETTINGS
SMS_DEBUG = True
SMS_CODE_KEY_PREFIX = 'sms_code_'
SMS_CODE_POOL = 'sms_code_pool'
SMS_CODE_POOL_OPEN = True
SMS_CODE_TIMEOUT = 60 * 30


# Captcha
GOOGLE_VERIFICATION_URL = 'https://www.google.com/recaptcha/api/siteverify'
GOOGLE_SITE_KEY = '6Lfc3G0fAAAAAFu5s67Q_-7ewZLlRvC1WVSo28pJ'
GOOGLE_SITE_SECRET = '6Lfc3G0fAAAAAHhosJFuakGWMDYy6_z9LcbSvgI4'


# API settings
APP_KEY_TO_SECRET = {
    'd41d8cd98f00b204e9800998ecf8427e': '75d78bdb89dd0baeaeacdbef66ba4240',
    '49438a211cf5b56937dea9a9917bcd40': 'adf51cf86a43f24947aa83303e7b025f',
}

JWT_SECRET = '69034aab94fa59e9104e95446234f887'


# Logging
system_string = platform.system()
if system_string == 'Linux':
    syslog_path = '/dev/log'
elif system_string == 'Darwin':
    syslog_path = '/var/run/syslog'
else:
    raise Exception('nonsupport platform!')

LOGGING_LEVEL = 'INFO'
LOGGING_LEVEL_SENTRY = 'ERROR'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s][%(msecs)03d] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': LOGGING_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'syslog': {
            'level': LOGGING_LEVEL,
            'class': 'logging.handlers.SysLogHandler',
            'facility': SysLogHandler.LOG_LOCAL2,
            'formatter': 'verbose',
            'address': syslog_path,
        },
        # 'sentry': {
        #     'level': LOGGING_LEVEL_SENTRY,
        #     'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        #     'tags': {'custom-tag': 'x'},
        # },
    },
    'loggers': {
        '': {
            'handlers': ['console', ],
            'level': LOGGING_LEVEL,
        },
        'django': {
            'handlers': ['console', ],
            'propagate': True,
            'level': LOGGING_LEVEL,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':LOGGING_LEVEL,
        },
        'celery.task': {
            'handlers': ['console', ],
            'propagate': True,
            'level': LOGGING_LEVEL,
        }
    }
}

# pagination
PAGE_SIZE = 10

# middle ware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# session settings
SESSION_COOKIE_AGE = 3600 * 24 * 365 * 10
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = 'session'
SESSION_SAVE_EVERY_REQUEST = True
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

OPENAI_API_KEY = ""
OPENAI_HOST = "https://api.openai.com/"
