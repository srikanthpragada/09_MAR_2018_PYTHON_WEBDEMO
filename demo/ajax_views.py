from django.shortcuts import render, HttpResponse
from demo.models import Course
from datetime import datetime


def ajax(request):
    return render(request, 'demo/ajax/ajax.html')


def today(request):
    now = datetime.now()
    return HttpResponse(now)


def get_name(request, id):
    # do
    return HttpResponse("abc")
