import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gameProject.settings')

app = Celery('gameProject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

from . import tasks


# docker run -p 6379:6379 redis
# python -m celery -A gameProject worker --loglevel=info --pool=solo -E
# python -m celery -A gameProject beat --loglevel=info


