
from django.contrib import admin
from django.urls import path
from demo.views import hello, wish, course

urlpatterns = [
    path('hello/', hello),
    path('wish/', wish),
    path('course/', course),
]
