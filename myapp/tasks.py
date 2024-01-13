from celery import shared_task 
from time import sleep


@shared_task
def sub ( x , y):
    sleep (15)
    return x-y

# the priodic schedule methord 1
@shared_task
def clear_session_cache(id):
    print ( 'the seccion is clear')
    return id