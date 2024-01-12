from django.shortcuts import render
from mycelerypro.celery import add 
from .tasks import sub
from celery.result import AsyncResult

## Create your views here.
# def index(request):
#     print("Result:")

#     # Call the Celery task asynchronously
#     result = add.delay(10, 20) #that send in the queue 
#     print("Task1 ID:", result.id)
#     result1 = sub.delay(10, 20) #that send in the queue 
#     print("Task2 ID:", result1.id)

#     return render(request, "myapp/home.html")

def index(request):
    print("Result:")

    # Call the Celery task asynchronously
    result = add.delay(10, 20) #that send in the queue 
    print("Task1 ID:", result.id)
    result1 = sub.delay(10, 20) #that send in the queue 
    print("Task2 ID:", result1.id)

    return render(request, "myapp/home.html")

def check_result ( request , task_id):
    result = AsyncResult ( task_id)
    print (result )
    return ( request , 'myapp/check_result' , {"result":result})


def contact( request):  
    print("Result:")
    return render ( request , "myapp/contact.html"  )

def about( request):
    print("Result:")
    return render ( request , "myapp/about.html"  ) 