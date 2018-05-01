from django.contrib import admin
from django.urls import path, re_path
from demo.views import hello, wish, course, list_courses, prime
from demo.cookie_views import show, selectcolor, selectcity, \
    showmovies, languages, clear
from .hr_views import add_dept, add_emp, list_dept, list_emp, search, get_employees
import demo.ajax_views as ajax_views
import demo.orm_views as orm_views
import demo.rest_views as rest_views

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
    path('add_emp/', add_emp),
    path('list_dept/', list_dept),
    path('search_emp/', search),
    path('today/', ajax_views.today),
    path('ajax/', ajax_views.ajax),
    re_path('getname/(\d+)', ajax_views.get_name),
    re_path(r'list_emp/(\d+)', list_emp),
    re_path(r'get_employees/(\w+)', get_employees),
    re_path(r'orm/empbydept/(\d+)', orm_views.emp_by_dept),
    path('orm/list_dept/', orm_views.list_dept),
    path('orm/list_emp/', orm_views.list_emp),
    path('orm/add_dept/', orm_views.add_dept),
    path('orm/home/', orm_views.home),
    path('orm/add_emp/', orm_views.add_emp),
    path('api/client/', rest_views.client),
    path('api/departments/', rest_views.list_dept),
    path('api/departments/<int:id>', rest_views.department_details),



]
