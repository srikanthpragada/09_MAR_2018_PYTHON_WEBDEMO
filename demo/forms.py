import django.forms as forms
import sqlite3


# Django form to take data about new department
class AddDeptForm(forms.Form):
    deptid = forms.IntegerField(label='Dept ID')
    deptname = forms.CharField(label='Dept Name', max_length=20)


class AddEmpForm(forms.Form):
    ename = forms.CharField(label="Full Name", max_length=20)
    salary = forms.IntegerField(label="Salary", min_value=5000)
    depts = []
    try:
        con = sqlite3.connect(r"e:\classroom\python\hr.db")
        cur = con.cursor()
        cur.execute("select * from dept order by id")
        depts = cur.fetchall()
    except Exception as ex:
        print("Error : ", ex)
    finally:
        con.close()

    dept = forms.ChoiceField(label="Department", choices=depts)
