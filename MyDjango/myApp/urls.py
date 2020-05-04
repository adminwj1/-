from django.urls import path
from myApp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('myApp', views.detail, name='detail'),
    path('grades', views.grades),
    path('students', views.students),
    path('addstudent', views.addstudent),
    path('addstudent2', views.addstudent2),
    path('students1', views.students1),
]