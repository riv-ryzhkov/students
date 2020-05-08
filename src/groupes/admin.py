from django.contrib import admin

from groupes.models import Groupe
from teachers.models import Teacher
from teachers.models import Logger
from teachers.forms import TeacherForm


class GroupeAdmin(admin.ModelAdmin):
    list_display = ('name', 'head', 'head_teach', 'phone', 'head_teach')
    # readonly_fields = ('phone', )
    list_select_related = ('head_teach', )
    list_per_page = 10
    search_fields = ('name', )
    ordering = ('name', )



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    # readonly_fields = ('phone', )
    list_per_page = 10
    form = TeacherForm

class LoggerAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'time_delta', 'created')
    list_per_page = 10




admin.site.register(Teacher, TeacherAdmin)

admin.site.register(Groupe, GroupeAdmin)

admin.site.register(Logger, LoggerAdmin)

# Register your models here.
