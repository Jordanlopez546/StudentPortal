from django.contrib import admin
from .models import *

class StudentProfilePanel(admin.ModelAdmin):
    list_display = ['user', 'dob', 'gender', 'phone_number', 'nationality']
    list_filter = ['nationality', 'status', 'created_at', 'course']
    search_fields = ['user__username', 'phone_number', 'nationality']

class CoursePanel(admin.ModelAdmin):
    list_display = ['course', 'class_size', 'lecturer', 'time', 'venue', 'room']
    list_filter = ['time', 'venue', 'room', 'lecturer']
    search_fields = ['course', 'lecturer', 'day']

class CourseRegistrationPanel(admin.ModelAdmin):
    list_display = ['student', 'the_course']
    list_filter = ['the_course']
    search_fields = ['student__user__username', 'the_course__course']
    
class GradePanel(admin.ModelAdmin):
    search_fields = ['student__user__username', 'the_course__course', 'grade']
    list_display = ['student', 'the_course', 'test_score', 'exam_score', 'total_score', 'gpa', 'grade']
    list_filter = ['student', 'the_course', 'grade']

admin.site.register(StudentProfile, StudentProfilePanel)
admin.site.register(Course, CoursePanel)
admin.site.register(CourseRegistration, CourseRegistrationPanel)
admin.site.register(Grade, GradePanel)