from rest_framework import serializers
from student.models import Student
from course.models import Course
from classperiod.models import Classperiod
from teacher.models  import  Teacher
from classes.models import Classes

class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classperiod
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "_ _all_ _"  

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "_ _all_ _"




class MinimalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name','email']

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'description']

class MinimalClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classperiod
        fields = ['day', 'time', 'class_instance']

class MinimalClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['name', 'description']

class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']