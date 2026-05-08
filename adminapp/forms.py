from django import forms
from .models import *


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class KafedraForm(forms.ModelForm):
    class Meta:
        model = Kafedra
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "faculty": forms.Select(attrs={'class': 'form-control'})
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control'}),
            "kafedra": forms.Select(attrs={'class': 'form-control'}),
            "hire_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "code": forms.TextInput(attrs={'class': 'form-control'}),
            "credits": forms.NumberInput(attrs={'class': 'form-control'}),
            "kafedra": forms.Select(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "faculty": forms.Select(attrs={'class': 'form-control'}),
            "created_year": forms.NumberInput(attrs={'class': 'form-control'}),
            "is_active": forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control'}),
            "birth_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "student_id": forms.TextInput(attrs={'class': 'form-control'}),
            "group": forms.Select(attrs={'class': 'form-control'}),
            "enrollment_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
