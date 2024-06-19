from django.db import models

# Create your models here.

class Teacher(models,Model):
    prefix = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    course_teaching = models.CharField(max_length=30) 
    email= models.EmailField()
    nationality = models.CharField(max_length=20)
    teacher_id = models.PositiveSmallIntegerField()
    Gender = models.CharField(max_length=20)
    Year_of_experience= models.PositiveSmallIntegerFiled()
    account_number = models.PositiveSmallIntegerFiled()

     def __str__(self):
        return f"{self.course_Id} {self.Course_name}"