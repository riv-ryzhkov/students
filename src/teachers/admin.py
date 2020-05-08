from django.contrib import admin

from teachers.models import Teacher
from teachers.models import Logger



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'emal')
    pass


class LoggerAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'time_delay', 'created')

# admin.site.register(Teacher, TeacherAdmin)
# Register your models here.
