from django.shortcuts import render, HttpResponse
from demo.models import Course
from datetime import datetime
import math


# Create your views here.

def hello(request):
    if "name" in request.GET:
        name = request.GET["name"]
    else:
        name = "World!"

    return HttpResponse("<h1>Hello %s </h1>" % (name))


def wish(request):
    ct = datetime.now()
    if ct.hour < 12:
        msg = "Good Morning!"
    elif ct.hour < 17:
        msg = "Good Afternoon!"
    else:
        msg = "Good Evening!"

    return HttpResponse("<h1>{}</h1>".format(msg))


def course(request):
    c = Course("Angular", 3000)
    return render(request, 'demo/course.html', {"course": c})


def list_courses(request):
    courses = [Course("Angular", 3000), Course("Python", 6000), Course("Java EE", 8000)]
    return render(request, 'demo/list_courses.html', {"courses": courses})


def prime(request):
    context = dict()
    context["message"] = ""
    if request.method == "GET":
        return render(request, 'demo/prime.html', context)
    else:  # POST
        # read data and process
        context["num"] = request.POST["num"]
        try:
            num = int(request.POST["num"])  # convert string to int
            context["message"] = "A Prime Number"
            for i in range(2, math.trunc(math.sqrt(num) + 1)):
                if num % i == 0:
                    context["message"] = "Not A Prime Number"
                    break
        except:
            context["message"] = "Sorry! Could not convert given input to number!"

        return render(request, 'demo/prime.html', context)



