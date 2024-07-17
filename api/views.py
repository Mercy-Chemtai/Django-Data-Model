from django.shortcuts import render

# Create your views here.


from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student
from .serializers  import StudentSerializer

from course.models import Course
from .serializers import CourseSerializer

from classperiod.models import Classperiod
from .serializers import  ClassperiodSerializer

from  classes.models import Classes
from .serializers import  ClassesSerializer

from  teacher.models import Teacher
from .serializers import  TeacherSerializer





class ClassperiodListView(APIView):
    def get(self,  request):
        Classperiod = Classperiod.objects.all()
        serializer = ClassperiodSerializer(Classperiod, many=True)

        return Response(serializer.data)


class StudentListView(APIView):
    def get(self,  request):
            student = Student.objects.all()
            serializer = StudentSerializer(Student, many=True)

            return Response(serializer.data)

class CourseListView(APIView):
        def get(self,request):
            Course = Course.Objects.all()
            serializer = CourseSerializer(Course,many=True)

            return Response (serializer.data)


class ClassesListView(APIView):
    def get(self,  request):
            Classes = Classes.objects.all()
            serializer = ClassesSerializer(Classes, many=True)

            return Response(serializer.data)            


class TeacherListView(APIView):
    def get(self,  request):
            Teacher = Teacher.objects.all()
            serializer = TeacherSerializer(Teacher, many=True)

            return Response(serializer.data)            


     
      


    


