from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from classperiod.models import Classperiod
from .serializers import  ClassperiodSerializer
class ClassperiodListView(APIView):
    def get(self,  request):
        Classperiod = Classperiod.objects.all()
        serializer = ClassperiodSerializer(Classperiod, many=True)

        return Response(serializer.data)


class StudentListView(APIView):
    def get(self,  request):
            Student = Student.objects.all()
            serializer = StudentSerializer(Student, many=True)

            return Response(serializer.data)



    


