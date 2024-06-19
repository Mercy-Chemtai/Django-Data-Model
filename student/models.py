from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email= models.EmailField()
    nationality = models.CharField(max_length=20)
    age = models.models.PositiveSmallIntegerField()
    Student_id = models.PositiveSmallIntegerField()
    Gender = models.CharField(max_length=20)
    Student_class = models.CharField(max_length=20)
    course_taking = models.CharField(max_length=20)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"




















































    
