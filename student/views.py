from django.shortcuts import render , redirect 
from django.http import HttpResponse 
from .models import student , Course
from .forms import StudentForm 


def add_student(request):
   # students =student.objects.all()
    if request.method == 'POST' :
        form = StudentForm(request.POST)
        if form.is_valid():           
            form.save()
            return redirect('students')
    else:
         form = StudentForm()
    return render(request , 'student/student.html' , {'form' : form})

def student_detail(request, student_name):
    students = student.objects.get(student , name = student_name)
    return render(request, 'student_detail.html', {'student': students})

#def student_by_name(request):
   # student_name = student.objects.filter(name = 'hager')
   # return render(request , 'student/student_name.html' , {'student_name' : student_name})



