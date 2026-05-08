from django.db import models


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='kafedralar', null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE, related_name='teachers', null=True)
    hire_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    code = models.CharField(max_length=10, unique=True, null=True)
    credits = models.PositiveIntegerField(default=1)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE, related_name='subjects', null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Group(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='groups', null=True)
    created_year = models.PositiveIntegerField(default=2024)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students', null=True)
    enrollment_date = models.DateField(null=True)
    student_id = models.CharField(max_length=20, unique=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
