from .base import *

DJANGO_ENV = "deploy"

DEBUG = False

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": "django",
        "HOST": "postgresdb",
        "PORT": "5432",
    }
}


# Elasticsearch
if "test" in sys.argv or "test_coverage" in sys.argv:  # Running tests
    ELASTICSEARCH_DSL = {
        "default": {
            "hosts": "elasticsearch:9200",
            "index_prefix": "test",
        },
    }
else:
    ELASTICSEARCH_DSL = {
        "default": {
            "hosts": "elasticsearch:9200",
            "index_prefix": "",
        },
    }


# celery
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"


# redis cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
