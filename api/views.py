from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student
from course.models import Course
from classperiod.models import Classperiod
from classes.models import Classes
from teacher.models import Teacher

from .serializers import StudentSerializer, CourseSerializer, ClassperiodSerializer, ClassesSerializer, TeacherSerializer

class ClassperiodListView(APIView):
    def get(self, request):
        class_periods = Classperiod.objects.all()
        serializer = ClassperiodSerializer(class_periods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassperiodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassperiodDetailView(APIView):
    def get(self, request, id):
        class_period = get_object_or_404(Classperiod, id=id)
        serializer = ClassperiodSerializer(class_period)
        return Response(serializer.data)

    def put(self, request, id):
        class_period = get_object_or_404(Classperiod, id=id)
        serializer = ClassperiodSerializer(class_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        class_period = get_object_or_404(Classperiod, id=id)
        class_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        course_id = request.data.get("course_id")
        class_id = request.data.get("class_id")

        if class_id:
            class_obj = get_object_or_404(Classes, id=class_id)
            student.classes.add(class_obj)  
            student.save() 
            return Response({'message': f'Student {student.id} added to class {class_id}'}, status=status.HTTP_200_OK)
        return Response({'error': 'class_id is required'}, status=status.HTTP_400_BAD_REQUEST)

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, id):
        course = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = get_object_or_404(Course, id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassesDetailView(APIView):
    def get(self, request, id):
        classes = get_object_or_404(Classes, id=id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)

    def put(self, request, id):
        classes = get_object_or_404(Classes, id=id)
        serializer = ClassesSerializer(classes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classes = get_object_or_404(Classes, id=id)
        classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherCourseAssignmentView(APIView):
    def post(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        course_id = request.data.get('course_id')

        if course_id:
            course = get_object_or_404(Course, id=course_id)
            teacher.courses.add(course)
            return Response({'message': f'Teacher {teacher_id} assigned to course {course_id}'}, status=status.HTTP_200_OK)

        return Response({'error': 'course_id is required'}, status=status.HTTP_400_BAD_REQUEST)

class TeacherTimetableView(APIView):
    def get(self, request, teacher_id):
        class_periods = Classperiod.objects.filter(teacher_id=teacher_id)
        
        classroom_data = []
        for period in class_periods:
            classroom_data.append({
                'class_id': period.class_instance.id,
                'course_id': period.course.id,
                'day': period.day,
                'time': period.time,
            })

        return Response({'teacher_id': teacher_id, 'timetable': classroom_data})