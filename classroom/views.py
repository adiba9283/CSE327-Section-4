from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from classroom.forms import UserForm,NoticeForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse
from classroom import models
from classroom.models import StudentsInClass,Student,Teacher
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q



## For writing notice which will be sent to all class students.
@login_required
def add_notice(request):
    notice_sent = False
    teacher = request.user.Teacher
    students = StudentsInClass.objects.filter(teacher=teacher)
    students_list = [x.student for x in students]

    if request.method == "POST":
        notice = NoticeForm(request.POST)
        if notice.is_valid():
            object = notice.save(commit=False)
            object.teacher = teacher
            object.save()
            object.students.add(*students_list)
            notice_sent = True
    else:
        notice = NoticeForm()
    return render(request,'classroom/write_notice.html',{'notice':notice,'notice_sent':notice_sent})

    ## Student can see all notice given by their teacher.
@login_required
def class_notice(request,pk):
    student = get_object_or_404(models.Student,pk=pk)
    return render(request,'classroom/class_notice_list.html',{'student':student})


## List of all students that teacher has added in their class.
def class_students_list(request):
    query = request.GET.get("q", None)
    students = StudentsInClass.objects.filter(teacher=request.user.Teacher)
    students_list = [x.student for x in students]
    qs = Student.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(name__icontains=query)
                )
    qs_one = []
    for x in qs:
        if x in students_list:
            qs_one.append(x)
        else:
            pass
    context = {
        "class_students_list": qs_one,
    }
    template = "classroom/class_students_list.html"
    return render(request, template, context)

class ClassStudentsListView(LoginRequiredMixin,DetailView):
    model = models.Teacher
    template_name = "classroom/class_students_list.html"
    context_object_name = "teacher"

## List of students which are not added by teacher in their class.
def students_list(request):
    query = request.GET.get("q", None)
    students = StudentsInClass.objects.filter(teacher=request.user.Teacher)
    students_list = [x.student for x in students]
    qs = Student.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(nameicontains=query)
                )
    qs_one = []
    for x in qs:
        if x in students_list:
            pass
        else:
            qs_one.append(x)

    context = {
        "students_list": qs_one,
    }
    template = "classroom/students_list.html"
    return render(request, template, context)

## List of all the teacher present in the portal.
def teachers_list(request):
    query = request.GET.get("q", None)
    qs = Teacher.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(nameicontains=query)
                )

    context = {
        "teachers_list": qs,
    }
    template = "classroom/teachers_list.html"
    return render(request, template, context)

