from django.http import HttpResponse
from django.views import View
from datetime import datetime
from django.views.generic import ListView
from demo.models import Department


class TodayView(View):
    def get(self, request):
        return HttpResponse(str(datetime.now()))


class DepartmentList(ListView):
    model = Department
    # template_name = 'demo/list_dept.html'
