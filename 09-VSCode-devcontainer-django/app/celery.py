import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings

app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()