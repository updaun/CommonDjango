from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from django.conf import settings

DJANGO_ENV = os.environ.get("DJANGO_ENV", "local")

settings_module = f"config.settings.{DJANGO_ENV}"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
