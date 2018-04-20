from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .forms import AddDeptForm, AddEmpForm
import sqlite3


def list_emp(request, id):
    employees = []
    try:
        con = sqlite3.connect(r"e:\classroom\python\hr.db")
        cur = con.cursor()
        # take input from user
        cur.execute("select * from emp where deptid = ?", (id))
        employees = cur.fetchall()
    except Exception as ex:
        print("Error : ", ex)
    finally:
        con.close()

    return render(request, 'demo/hr/list_emp.html',
                  {"employees": employees, 'deptid': id})


def list_dept(request):
    depts = []
    try:
        con = sqlite3.connect(r"e:\classroom\python\hr.db")
        cur = con.cursor()
        # take input from user
        cur.execute("select * from dept")
        depts = cur.fetchall()
        print(depts)
    except Exception as ex:
        print("Error : ", ex)
    finally:
        con.close()

    return render(request, 'demo/hr/list_dept.html', {"depts": depts})


def add_dept(request):
    if request.method == "POST":
        form = AddDeptForm(request.POST)
        message = ""
        if form.is_valid():
            id = form.cleaned_data["deptid"]
            name = form.cleaned_data["deptname"]
            # insert row into DEPT table
            try:
                con = sqlite3.connect(r"e:\classroom\python\hr.db")
                cur = con.cursor()
                # take input from user
                cur.execute("insert into dept values(?,?)", (id, name))
                con.commit()
                return HttpResponseRedirect('/demo/list_dept/')
            except Exception as ex:
                print("Error : ", ex)
                message = "Error : " + str(ex)
            finally:
                con.close()

        return render(request, 'demo/hr/add_dept.html', {'form': form, 'message': message})
    else:  # GET
        form = AddDeptForm()  # empty form
        return render(request, 'demo/hr/add_dept.html', {'form': form})


def add_emp(request):
    if request.method == "POST":
        form = AddEmpForm(request.POST)
        message = ""
        if form.is_valid():
            ename = form.cleaned_data["ename"]
            salary = form.cleaned_data["salary"]
            dept = form.cleaned_data["dept"]

            # insert row into EMP table
            try:
                con = sqlite3.connect(r"e:\classroom\python\hr.db")
                cur = con.cursor()
                # Find out next empid
                cur.execute("select max(empid) + 1 from emp")
                empid = cur.fetchone()[0]
                cur.execute("insert into emp values(?,?,?,?)",
                            (empid, ename, salary, dept))
                con.commit()
                message = "Employee [%d] has been inserted!" % (empid)
            except Exception as ex:
                print("Error : ", ex)
                message = "Error : " + str(ex)
            finally:
                con.close()
        else:
            print(form.errors)

        return render(request, 'demo/hr/add_emp.html',
                      {'form': form, 'message': message})
    else:
        form = AddEmpForm()  # empty form
        return render(request, 'demo/hr/add_emp.html', {'form': form})

def search(request):
    return render(request, 'demo/hr/search_emp.html')

def get_employees(request, name):
    name = "%" + name + "%"
    print(name)
    employees = []
    try:
        con = sqlite3.connect(r"e:\classroom\python\hr.db")
        cur = con.cursor()
        # take input from user
        cur.execute("select * from emp where empname like ?",(name,))
        employees = cur.fetchall()
    except Exception as ex:
        print("Error in search  : ", ex)
    finally:
        con.close()

    return JsonResponse(employees, safe=False)
