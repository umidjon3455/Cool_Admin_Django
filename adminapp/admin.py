from django.contrib import admin
from .models import Faculty, Kafedra, Teacher, Subject, Group, Student


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')
    list_filter = ('faculty',)
    search_fields = ('name', 'faculty__name')
    ordering = ('faculty', 'name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'kafedra', 'hire_date')
    list_filter = ('kafedra', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')
    date_hierarchy = 'hire_date'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'credits', 'kafedra')
    list_filter = ('kafedra', 'credits')
    search_fields = ('name', 'code', 'kafedra__name')
    ordering = ('code', 'name')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'created_year', 'is_active')
    list_filter = ('faculty', 'is_active', 'created_year')
    search_fields = ('name', 'faculty__name')
    ordering = ('faculty', 'name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email', 'group', 'enrollment_date')
    list_filter = ('group', 'group__faculty', 'enrollment_date')
    search_fields = ('first_name', 'last_name', 'student_id', 'email')
    ordering = ('last_name', 'first_name')
    date_hierarchy = 'enrollment_date'
