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




@shared_task(name='gameProject.test_time')
def test_time():
    from profiles.models import Profile
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.trips < 32:
            profile.trips += 1
            profile.save()
            print(f"Profile {profile.name} now has {profile.trips} trips.")
    print("added trip to each profile")
