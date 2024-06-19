from django.db import models

# Create your models here.

class course(models,Model):
    Course_name = models.CharField(max_length=10)
    students_taking = models.PositiveSmallIntegerFiled()
    course_Id = models.PositiveSmallIntegerFiled()
    Class_teacher CharField(max_length=10)
    school_name = CharField(max_length=10)
    course_passmark = PositiveSmallIntegerFiled()
    capacity = models.PositiveSmallIntegerFiled()
    class_time = models.PositiveSmallIntegerFiled()
    room_number = models.PositiveSmallIntegerFiled()
    Academic_year = models.PositiveSmallIntegerFiled()

     def __str__(self):
        return f"{self.course_Id} {self.Course_name}"

