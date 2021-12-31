from django import forms
from django.contrib.auth.forms import UserCreationForm
from classroom.models import User,StudentMarks,MessageToTeacher
from django.db import transaction

## User Login Form (Applied in both student and teacher login)
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']
        widgets = {
                'username': forms.TextInput(attrs={'class':'answer'}),
                'password1': forms.PasswordInput(attrs={'class':'answer'}),
                'password2': forms.PasswordInput(attrs={'class':'answer'}),
                }


        
## Form for uploading marks and also for updating it.
class MarksForm(forms.ModelForm):
    class Meta():
        model = StudentMarks
        fields = ['subject_name','marks_obtained','maximum_marks']

## Writing message to teacher        
class MessageForm(forms.ModelForm):
    class Meta():
        model = MessageToTeacher
        fields = ['message']


