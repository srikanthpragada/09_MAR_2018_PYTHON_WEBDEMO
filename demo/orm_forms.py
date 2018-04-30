from django.forms import ModelForm
from demo.models import Department, Employee

# Model form - form driven by model

class AddDeptForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"



class AddEmpForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
