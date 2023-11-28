from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'teacher_name']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['kids_circle', 'date', 'time']

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'patronymic', 'birth_date']

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['schedule', 'child']
