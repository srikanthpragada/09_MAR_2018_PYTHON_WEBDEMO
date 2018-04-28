from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from demo.models import Department, Employee
from django.http import JsonResponse
from .forms import AddDeptForm, AddEmpForm


def list_emp(request):
    pass


def list_dept(request):
    try:
        depts = Department.objects.all()
    except Exception as ex:
        print("Error : ", ex)

    return render(request, 'demo/orm/list_dept.html', {"depts": depts})
