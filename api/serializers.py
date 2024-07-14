from rest_framework import serializers
from student.models import Student
from classperiod.models import Classperiod

class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = classmethod
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
