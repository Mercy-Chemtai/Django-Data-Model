from rest_framework import serializers
from student.models import Student
from course.models import Course
from classperiod.models import Classperiod
from teacher.models import Teacher
from classes.models import Classes

class MinimalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "email"]

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "description"]

class MinimalClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classperiod
        fields = ["id", "day", "time"]

class MinimalClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ["id", "name"]

class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name"]




class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classperiod
        fields = ["id", "start_time", "end_time", "day", "classes"]

class CourseSerializer(serializers.ModelSerializer):
    classperiods = ClassperiodSerializer(many=True)
    classes = serializers.PrimaryKeyRelatedField(many=True, queryset=Classes.objects.all()) 
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all()) 

    class Meta:
        model = Course
        fields = ["id", "name", "description", "classperiods", "classes", "teacher"]

class TeacherSerializer(serializers.ModelSerializer):
    students = MinimalStudentSerializer(many=True)
    classes = serializers.PrimaryKeyRelatedField(many=True, queryset=Classes.objects.all()) 
    courses = CourseSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ["id", "name", "email", "students", "classes", "courses"]

class ClassesSerializer(serializers.ModelSerializer):
    students = MinimalStudentSerializer(many=True)
    classperiods = ClassperiodSerializer(many=True)
    course = CourseSerializer()

    class Meta:
        model = Classes
        fields = ["id", "name", "classperiods", "course", "students"]

class StudentSerializer(serializers.ModelSerializer):
    classperiods = ClassperiodSerializer(many=True)
    courses = CourseSerializer(many=True)
    teacher = TeacherSerializer()
    classes = ClassesSerializer(many=True)

    class Meta:
        model = Student
        fields = ["id", "name", "email", "classperiods", "courses", "teacher", "classes"]