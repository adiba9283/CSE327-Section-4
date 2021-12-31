from django.urls import path
from classroom import views

app_name = 'classroom'

urlpatterns =[
    path('upload_assignment/',views.upload_assignment,name="upload_assignment"),
    path('class_assignment/',views.class_assignment,name="class_assignment"),
    path('assignment_list/',views.assignment_list,name="assignment_list"),
    path('update_assignment/<int:id>/',views.update_assignment,name="update_assignment"),
    path('assignment_delete/<int:id>/',views.assignment_delete,name="assignment_delete"),
    path('submit_assignment/<int:id>/',views.submit_assignment,name="submit_assignment"),
    path('submit_list/',views.submit_list,name="submit_list"),
    path('change_password/',views.change_password,name="change_password"),
]
