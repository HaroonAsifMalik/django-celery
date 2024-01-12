from celery import shared_task 
from time import sleep


@shared_task
def sub ( x , y):
    sleep (15)
    return x-y