# Generated by Django 2.2.11 on 2020-05-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_logger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='method',
            field=models.CharField(default='mmmmmm', max_length=128),
        ),
        migrations.AlterField(
            model_name='logger',
            name='path',
            field=models.CharField(default='pppppp', max_length=128),
        ),
        migrations.AlterField(
            model_name='logger',
            name='time_delta',
            field=models.CharField(default='tttttt', max_length=128),
        ),
    ]
