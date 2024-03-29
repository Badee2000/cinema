import os
from celery import Celery
from celery.schedules import crontab

# In order to use celery you should do this:


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema.settings')


# create an instance of the application.
app = Celery('cinema')

# By setting the CELERY namespace,
# all Celery settings need to include the CELERY_ prefix in their name
app.config_from_object('django.conf:settings', namespace='CELERY')

# look for a tasks.py file in each application directory
app.autodiscover_tasks()

# This command will run immediatly after starting celery worker and beat in terminals.
app.conf.beat_schedule = {
    "update_rankings": {
        "task": "movies.tasks.update_movie_rankings",
        "schedule": crontab(minute='*/5'),  # Every 5 minute
    }
}
