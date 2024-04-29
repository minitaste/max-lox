from django.contrib.auth.models import User
from django.db import models
from group.models import Group
from professor.models import Course

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=None)
    email = models.EmailField(unique=True, default="") 
    chief = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.FloatField()

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.course.course_name}: {self.grade}"