# from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cnho.settings')

app = Celery('cnho',
             broker_url=os.getenv("CELERY_BROKER_URL",
                                  'redis://127.0.0.1:6379'),
             result_backend=os.getenv("CELERY_RESULT_BACKEND",
                                      'redis://127.0.0.1:6379'),
             redis_backend_health_check_interval=30,
             accept_content=['application/json'],
             result_serializer='json',
             task_serializer='json',
             timezone='Europe/Moscow',
             )

app.conf.update(
    result_expires=3600,
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    'add_subscriber': {
        'task': 'mailing.tasks.add_subscriber',
        'schedule': crontab(minute=0, hour=0)
    },
}
app.conf.timezone = 'UTC'
