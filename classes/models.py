from django.db import models

# Create your models here.

class Classes(models.Model):
    Class_name = models.CharField(max_length=10)
    Class_Id = models.IntegerField()
    Number_of_student = models.PositiveSmallIntegerField()
    courses = models.CharField(max_length=20)
    number_of_teachers = models.CharField(max_length=20)
    Room_number = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    Class_time  = models.CharField(max_length=20)
    Meeting_days = models.CharField(max_length=20)
    Attendance = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.Class_Id} {self.Class_name}"
