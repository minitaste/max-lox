from django.contrib.auth.models import User
from django.db import models


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=255, default="")
    position = models.CharField(max_length=150, default="")
    email = models.EmailField(unique=True, default="") 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    course_name = models.CharField(max_length=255, default="")
    credit = models.IntegerField()
    hours = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.course_name
    
