from django.db import models

# Create your models here.

class Class(models,Model):
    Class_name = models.CharField(max_length=10)
    Class_Id = models.PositiveSmallIntegerFiled()
    Number_of_student = models.PositiveSmallIntegerFiled()
    courses = models.CharField(max_length=20)
    number_of_teachers = models.CharField(max_length=20)
    Room_number = models.PositiveSmallIntegerFiled()
    capacity = models.PositiveSmallIntegerFiled()
    Class_time  = models.CharField(max_length=20)
    Meeting_days = models.CharField(max_length=20)
    Attendance = models.PositiveSmallIntegerFiled()

 def __str__(self):
        return f"{self.Class_Id} {self.Class_name}"
