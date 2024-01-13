import os
from time import sleep
from celery import Celery
from celery import timedelta 
from celery.schedule import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycelerypro.settings')

app = Celery('mycelerypro')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(name="addition_task")
def add(x, y):
    sleep(10) #for make it time consiming
    return x + y

#preodic function methord 2
# app.conf.beat_schedule = {
#     'every_10_second':{
#         'task':'myapp.tasks.clear_session_cache',
#         'schedule':10,
#         'args':(1111,)
#     }
#      # add other tasks ...
#  
# }

# #using timedelta
# app.conf.beat_schedule = {
#     'every_10_second':{
#         'task':'myapp.tasks.clear_session_cache',
#         'schedule':timedelta(seconds = 10),
#         'args':(1111,)
#     }
#      # add other tasks ...      
# }

#using timedelta
app.conf.beat_schedule = {
    'every_10_second':{
        'task':'myapp.tasks.clear_session_cache',
        'schedule':crontab(minute ='*/1'), # more advance scheduling
        'args':(1111,)
    }
     # add other tasks ...      
}
