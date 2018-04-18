import django.forms as forms


# Django form to take data about new department
class AddDeptForm(forms.Form):
    deptid = forms.IntegerField(label='Dept ID')
    deptname = forms.CharField(label='Dept Name', max_length=20)


class AddEmpForm(forms.Form):
    pass
