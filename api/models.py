from django.db import models

# Create your models here.

from django.db import models
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your models here.
class StudentSerializer(serializers.Modelserializer):
    class Meta:
        model = Student
        fields = "_ _all_ _"



Class StudentListView(APIView):
        def get(self,request):
            student = Student.Objects.all()
            serializer = StudentSerializer(students,many=True)
            return Response (serializer.data)
      



class TeacherSerializer(serializers.Modelserializer):
    class Meta:
        model = Teacher
        fields = "_ _all_ _"

class CourseSerializer(serializers.Modelserializer):
    class Meta:
        model = Course
        fields = "_ _all_ _"

class ClassSerializer(serializers.Modelserializer):
    class Meta:
        model = Student
        fields = "_ _all_ _"
