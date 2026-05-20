from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import teacher
from .forms import TeacherForm
# Create your views here.

def teacher_page(request):
    #teachers = teacher.objects.all()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm()


    return render(request , 'teacher/teacher.html' , {'form' : form})