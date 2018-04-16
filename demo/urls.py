
from django.contrib import admin
from django.urls import path
from demo.views import hello, wish, course, list_courses, prime
from demo.cookie_views import show, selectcolor, selectcity, showmovies

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
]
