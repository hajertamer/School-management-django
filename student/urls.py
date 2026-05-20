from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('' , views.add_student , name = 'students'),
    path('', views.student_detail, name='student_detail'),
    
]