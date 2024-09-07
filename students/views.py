from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Student
from django.urls import reverse
from .forms import StudentForm
# Create your views here.

def index(request):
    return render(request, 'index.html', {'students': Student.objects.all()})

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'view_student.html', {'student': student})

def add(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_middle_name = form.cleaned_data['middle_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_phone = form.cleaned_data['phone']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']
            
            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                middle_name = new_middle_name,
                last_name = new_last_name,
                email = new_email,
                phone = new_phone,
                field_of_study = new_field_of_study,
                gpa = new_gpa
            )
            new_student.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = StudentForm()
    return render(request, 'add.html', {
        'form': form
    })
    
def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form': form,
                'student': student,
                'success': True
            })
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {
        'form': form,
        'student': student
    })
    
def delete(request, id):
    # Delete the student record
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('index')
    return render(request, 'delete.html', {'student': student})