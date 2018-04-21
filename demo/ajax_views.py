from django.shortcuts import render, HttpResponse
from demo.models import Course
from datetime import datetime
import sqlite3


def ajax(request):
    return render(request, 'demo/ajax/ajax.html')


def today(request):
    now = datetime.now()
    return HttpResponse(now)


def get_name(request, id):
    print(id)
    result = ""
    try:
        con = sqlite3.connect(r"e:\classroom\python\hr.db")
        cur = con.cursor()
        cur.execute("select empname, salary from emp where empid = ?", (id,))
        emp = cur.fetchone()
        if emp == None:
            result = "Not Found"
        else:
            result = str(emp[0])  + " - " + str(emp[1])
    except Exception as ex:
        print("Error : ", ex)
        result = "Error"
    finally:
        con.close()

    return HttpResponse(result)
