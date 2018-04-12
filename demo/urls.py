
from django.contrib import admin
from django.urls import path
from demo.views import hello, wish, course, list_courses, prime

urlpatterns = [
    path('hello/', hello),
    path('wish/', wish),
    path('course/', course),
    path('listcourses/', list_courses),
    path('prime/', prime),
]
