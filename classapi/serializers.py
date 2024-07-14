from rest_framework import serializers
from student.models import Student

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"