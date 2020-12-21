import os
from math import sqrt

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'root_number.settings')

app = Celery('root_number')

# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.config_from_object()

app.autodiscover_tasks()

app.conf.broker_url = 'redis://@localhost:6379/0'
app.conf.broker_transport_options = {'visibility_timeout': 3600}
app.conf.result_backend = 'redis://localhost:6379/0'
app.conf.result_backend_transport_options = {
    'retry_policy': {
       'timeout': 5.0
    }
}

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Moscow',
    enable_utc=True,
)

app.conf.task_routes = {
    'tasks.root_of_number': 'low-priority',
}
