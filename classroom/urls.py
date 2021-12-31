from django.urls import path
from classroom import views

app_name = 'classroom'

urlpatterns =[

    path('teacher/write_notice',views.add_notice,name="write_notice"),
    path('student/<int:pk>/class_notice',views.class_notice,name="class_notice"),



]
