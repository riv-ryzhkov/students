# Generated by Django 2.2.11 on 2020-04-23 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200403_1511'),
        ('groupes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupe',
            name='head_teach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teachers.Teacher'),
        ),
    ]
