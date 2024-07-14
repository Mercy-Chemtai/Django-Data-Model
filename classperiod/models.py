from django.db import models

# Create your models here.

class Classperiod(models.Model):
    Course_name = models.CharField(max_length=10)
    Students_taking = models.IntegerField()
    Course_id = models.IntegerField()
    Class_teacher = models.CharField(max_length=20)
    number_of_teachers = models.CharField(max_length=20)
    Classroom = models.CharField(max_length=10)
    Start_time= models.TimeField()
    End_time= models.TimeField()
    Academic_year = models.CharField(max_length=20)
    Day_Of_The_Week = models.CharField(max_length=20)
    Capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.Class_Id} {self.Class_name}"
