from django.contrib import admin
from django.urls import path
from demo.views import hello, wish, course, list_courses, prime
from demo.cookie_views import show, selectcolor, selectcity, \
    showmovies, languages, clear
from .hr_views import add_dept

urlpatterns = [
    path('hello/', hello),
    path('wish/', wish),
    path('course/', course),
    path('listcourses/', list_courses),
    path('prime/', prime),
    path('show/', show),
    path('selectcolor/', selectcolor),
    path('selectcity/', selectcity),
    path('showmovies/', showmovies),
    path('langs/', languages),
    path('clear/', clear),
    path('add_dept/', add_dept),
]
