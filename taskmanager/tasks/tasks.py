from __future__ import absolute_import, unicode_literals

from datetime import datetime

from celery import shared_task

from .models import Test


@shared_task
def create_test_instance():
    Test.objects.create(name = str(datetime.now()))