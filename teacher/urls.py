from django.urls import path
from .views import teacher_page

urlpatterns = [
    path('' , teacher_page, name='teachers')
]