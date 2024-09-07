from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'middle_name', 'last_name', 'email', 'phone', 'field_of_study', 'gpa']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'middle_name': 'Middle Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Phone',
            'field_of_study': 'Field of Study',
            'gpa': 'GPA'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'middle_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class':'form-control'}),
            'gpa': forms.NumberInput(attrs={'class':'form-control'}),
        }