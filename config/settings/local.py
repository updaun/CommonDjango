from .base import *

DJANGO_ENV = "local"

DEBUG = True

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Elasticsearch
if "test" in sys.argv or "test_coverage" in sys.argv:  # Running tests
    ELASTICSEARCH_DSL = {
        "default": {
            "hosts": "localhost:9200",
            "index_prefix": "test",
        },
    }
else:
    ELASTICSEARCH_DSL = {
        "default": {
            "hosts": "localhost:9200",
            "index_prefix": "",
        },
    }

# celery
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")


# redis cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
