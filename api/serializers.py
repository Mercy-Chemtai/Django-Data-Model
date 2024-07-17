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


        