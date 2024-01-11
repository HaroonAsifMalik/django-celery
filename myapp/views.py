from django.shortcuts import render
from mycelerypro.celery import add
from celery.result import AsyncResult

# Create your views here.
def index(request):
    print("Result:")
    # Call the Celery task asynchronously
    result = add.delay(10, 20) #that send in the queue 

    print("Task ID:", result.id)

    return render(request, "myapp/home.html")


def contact( request):  
    print("Result:")
    return render ( request , "myapp/contact.html"  )

def about( request):
    print("Result:")
    return render ( request , "myapp/about.html"  ) 