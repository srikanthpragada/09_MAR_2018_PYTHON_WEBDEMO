from django.shortcuts import render, HttpResponse
from demo.models import Course


# Create your views here.

def hello(request):
    if "name" in request.GET:
        name = request.GET["name"]
    else:
        name = "World!"

    return HttpResponse("<h1>Hello %s </h1>" % (name))


def wish(request):
    return HttpResponse("Wishing...")


def course(request):
    c = Course("Angular", 3000)
    return HttpResponse("<h2>%s</h2>" % (str(c)))
