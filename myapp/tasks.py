from celery import shared_task 
from time import sleep


@shared_task
def sub ( x , y):
    sleep (15)
    return x-y

# priodic function task
@shared_task
def clear_session_cache(id):
    print ( 'the seccion is clear')
    return id

@shared_task
def clear_redis_data(key):
    print ( 'the seccion is clear')
    return key

