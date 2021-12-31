from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
import misaka


# Create your models here.




class ClassAssignment(models.Model):
    student = models.ManyToManyField(Student,related_name='student_assignment')
    teacher = models.ForeignKey(Teacher,related_name='teacher_assignment',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    assignment_name = models.CharField(max_length=250)
    assignment = models.FileField(upload_to='assignments')

    def __str__(self):
        return self.assignment_name

    class Meta:
        ordering = ['-created_at']

class SubmitAssignment(models.Model):
    student = models.ForeignKey(Student,related_name='student_submit',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,related_name='teacher_submit',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    submitted_assignment = models.ForeignKey(ClassAssignment,related_name='submission_for_assignment',on_delete=models.CASCADE)
    submit = models.FileField(upload_to='Submission')

    def __str__(self):
        return "Submitted"+str(self.submitted_assignment.assignment_name)

    class Meta:
        ordering = ['-created_at']
