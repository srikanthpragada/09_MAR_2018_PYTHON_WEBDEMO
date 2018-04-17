from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import AddDeptForm


def add_dept(request):
    form = AddDeptForm()
    return render(request, 'demo/hr/add_dept.html', {'form': form})
