from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from demo.models import Department, Employee
from demo.orm_forms import AddDeptForm, AddEmpForm


def list_emp(request):
    emps = Employee.objects.all()
    return render(request, 'demo/orm/list_emp.html', {"emps": emps})


def emp_by_dept(request, id):
    emps = Employee.objects.filter(department=id)
    return render(request, 'demo/orm/list_emp.html', {"emps": emps})


def add_emp(request):
    if request.method == "POST":
        form = AddEmpForm(request.POST)
        if form.is_valid():
            form.save()  # insert row into Employees table
            return HttpResponseRedirect("/demo/orm/home")
    else:
        form = AddEmpForm()

    return render(request, 'demo/orm/add_emp.html', {"form": form})


def add_dept(request):
    if request.method == "POST":
        form = AddDeptForm(request.POST)
        if form.is_valid():
            form.save()  # insert row into Departments table
            return HttpResponseRedirect("/demo/orm/home")
    else:
        form = AddDeptForm()

    return render(request, 'demo/orm/add_dept.html', {"form": form})


def home(request):
    dept_count = Department.objects.count()
    emp_count = Employee.objects.count()
    return render(request, 'demo/orm/home.html',
                  {"dept_count": dept_count,
                   "emp_count": emp_count})


def list_dept(request):
    depts = Department.objects.all()
    return render(request, 'demo/orm/list_dept.html', {"depts": depts})
