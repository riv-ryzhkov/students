# Generated by Django 2.2.11 on 2020-04-26 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groupes', '0002_groupe_head_teach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupe',
            name='head_teach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to='teachers.Teacher'),
        ),
    ]
