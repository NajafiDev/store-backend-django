import os
import dj_database_url
from .common import *

DEBUG = os.getenv("DEBUG", "False") == "True"

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "store-backend-django.onrender.com").split(",")

DATABASES = {
    "default": dj_database_url.config(default=os.getenv("postgresql://storeback_django_db_user:WmEwQEJsfUkwh9UTwaKk62QnqaEZD2im@dpg-d3pkq349c44c73c4cci0-a.frankfurt-postgres.render.com/storeback_django_db"))
}

REDIS_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
# EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
# EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
# EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']