# Generated by Django 2.2.11 on 2020-05-04 20:30

from django.db import migrations



def forwards(apps, shema_editor):
    Teacher = apps.get_model('teachers', 'Teacher')
    for teacher in Teacher.objects.exclude(first_name='').iterator():
        teacher = teacher.first_name.capitalize()
        teacher.save()
    for teacher in Teacher.objects.exclude(last_name='').iterator():
        teacher = teacher.last_name.capitalize()
        teacher.save()


def backwards(apps, shema_editor):
    print('backwards' * 15)


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20200504_0520'),
    ]

    operations = [
    ]
