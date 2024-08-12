from django.shortcuts import render
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student
from .serializers import StudentSerializer
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



    def post(self, request):
        serializer = ClassperiodSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        





class ClassperiodDetailView(APIView):
    def get(self, request , id):
        classperiod = Classperiod.objects.get(id=id)
        serializer = ClassperiodSerializer(classperiod)
        return Response(serializer.data)


    def put(self , request, id):
        serializer = classperiodSerializer(classperiod,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(Serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)  


    def delete(self , request, id):
        serializer = Classperiod.objects.get(id=id)
        return Response(status = status.HTTP_202_ACCEPTED)
                











class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request .query-params.get("first_name")
        if first_name:
            students= students.filter(first_name= first_name)
        if country:    
             students= students.filter(country = country)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  



class StudentDetailView(APIView):
    def get(self, request , id):
        students = Student.objects.get(id=id)
        serializer = StudentSerializer(students)
        return Response(serializer.data)


    def enroll_student(self, student,course_Id):
        course = Course.objects.get(id=course_id)
        student.course.add(course)

    def post(self ,request, id):
        student.objects.get(id = id)
        if action == "enroll":
           course_id = request.data.get("course")
           self.enroll_student(student,course_Id)
        return Response(status.HTTP_201_ACCEPTED)   






    def put(self , request, id):
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(Serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)  


    def delete(self , request, id):
        serializer = Student.objects.get(id=id)
        return Response(status = status.HTTP_202_ACCEPTED)
                















class CourseListView(APIView):
    def get(self,request):
            course = Course.objects.all()
            serializer = CourseSerializer(course,many=True)
            return Response (serializer.data)


    def post(self , request):
        serializer = CourseSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(Serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)  




class CourseDetailView(APIView):
    def get(self, request , id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


    def put(self , request, id):
        serializer = CourseSerializer(course,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(Serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)  


    def delete(self , request, id):
        serializer = Course.objects.get(id=id)
        return Response(status = status.HTTP_202_ACCEPTED)
                









class ClassesListView(APIView):
    def get(self,  request):
            classes = Classes.objects.all()
            serializer = ClassesSerializer(classes, many=True)

            return Response(serializer.data)    


def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ClassesDetailView(APIView):
    def get(self, request , id):
        classes = Classes.objects.get(id=id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)


    def put(self , request, id):
        serializer = ClassesSerializer(classes,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(Serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)  


    def delete(self , request, id):
        serializer = Classes.objects.get(id=id)
        return Response(status = status.HTTP_202_ACCEPTED)
                
















class TeacherListView(APIView):
    def get(self,  request):
            Teacher = Teacher.objects.all()
            serializer = TeacherSerializer(Teacher, many=True)

            return Response(serializer.data)  


    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class TeacherDetailView(APIView):
    def get(self, request , id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)


    def put(self , request, id):
        serializer = TeacherSerializer(teacher,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(Serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)  


    def delete(self , request, id):
        serializer = Teacher.objects.get(id=id)
        return Response(status = status.HTTP_202_ACCEPTED)
                                      


     
      


    


