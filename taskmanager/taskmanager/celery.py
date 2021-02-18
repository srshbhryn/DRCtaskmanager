import os

from celery import Celery
from celery import shared_task

from .settings import CELERY_BROKER, TIME_ZONE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

app = Celery('taskmanager', broker=CELERY_BROKER)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = TIME_ZONE

app.autodiscover_tasks()

