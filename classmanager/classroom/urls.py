from django.urls import path
from classroom import views

app_name = 'classroom'

urlpatterns =[
	
    path('student/<int:pk>/enter_marks',views.add_marks,name="enter_marks"),
    path('student/<int:pk>/marks_list',views.student_marks_list,name="student_marks_list"),
    path('marks/<int:pk>/update',views.update_marks,name="update_marks"),
    path('student/<int:pk>/all_marks',views.StudentAllMarksList.as_view(),name="all_marks_list"),
    
    path('student/<int:pk>/message',views.write_message,name="write_message"),
    path('teacher/<int:pk>/messages_list',views.messages_list,name="messages_list")
	
]
