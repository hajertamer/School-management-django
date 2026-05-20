from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=(50))
    time = models.TimeField()
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name
    
class student(models.Model):
    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name 
    
