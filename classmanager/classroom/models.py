from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
import misaka
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)



class StudentMarks(models.Model):
    teacher = models.ForeignKey(Teacher,related_name='given_marks',on_delete=models.CASCADE)
    student = models.ForeignKey(Student,related_name="marks",on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=250)
    marks_obtained = models.IntegerField()
    maximum_marks = models.IntegerField()

    def __str__(self):
        return self.subject_name

class StudentsInClass(models.Model):
    teacher = models.ForeignKey(Teacher,related_name="class_teacher",on_delete=models.CASCADE)
    student = models.ForeignKey(Student,related_name="user_student_name",on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

    class Meta:
        unique_together = ('teacher','student')
        


class MessageToTeacher(models.Model):
    student = models.ForeignKey(Student,related_name='student',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,related_name='messages',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['student','message']





