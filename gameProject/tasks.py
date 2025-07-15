# myapp/tasks.py
from celery import shared_task
from django.utils.timezone import now
import datetime

@shared_task
def hello_task():
    print(f"[{now()}] Hello from Celery task!")
    return "Task complete"


@shared_task(name='gameProject.print_time')
def print_time():
    now = datetime.datetime.now()
    print(f"[{now}] Zadanie wykonane!")
