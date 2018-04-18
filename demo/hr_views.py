from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddDeptForm
import sqlite3

def list_emp(request):
    print(request.GET.get("deptid",1))

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
