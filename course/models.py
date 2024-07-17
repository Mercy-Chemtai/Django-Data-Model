from django.db import models

# Create your models here.

class Course(models.Model):
    Course_name = models.CharField(max_length=10)
    students_taking = models.PositiveSmallIntegerField()
    course_Id = models.PositiveSmallIntegerField()
    class_teacher = models.CharField(max_length=10)
    school_name = models.CharField(max_length=10)
    course_passmark = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    class_time = models.PositiveSmallIntegerField()
    room_number = models.PositiveSmallIntegerField()
    Academic_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.course_Id} {self.Course_name}"

