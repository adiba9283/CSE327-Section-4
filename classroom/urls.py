from django.urls import path
from classroom import views

app_name = 'classroom'

urlpatterns =[

    path('teacher/write_notice',views.add_notice,name="write_notice"),
    path('student/<int:pk>/class_notice',views.class_notice,name="class_notice"),

    path('students_list/',views.students_list,name="students_list"),
    path('teachers_list/',views.teachers_list,name="teachers_list"),
    path('teacher/class_students_list',views.class_students_list,name="class_student_list")

]
