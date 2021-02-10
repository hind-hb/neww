from .models import Employee
from .Serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def EmpListapi(request):
    all_Emp = Employee.objects.all()
    data = EmpSerializer(all_Emp,many=True).data
    return Response({'data':data})

class Emp_list(generics.ListCreateAPIView):
    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer

