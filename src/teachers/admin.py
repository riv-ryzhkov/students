from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'emai')
    pass



# admin.site.register(Teacher, TeacherAdmin)
# Register your models here.
