from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from demo.models import Department
from demo.serializers import DepartmentSerializer


def client(request):
    return render(request, 'demo/restclient.html')


@api_view(['GET'])
def list_dept(request):
    depts = Department.objects.all()
    serializer = DepartmentSerializer(depts, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def department_details(request, id):
    """
    Retrieve or delete department
    """
    try:
        dept = Department.objects.get(pk=id)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DepartmentSerializer(dept)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        dept.delete()
        return Response(status=204)

