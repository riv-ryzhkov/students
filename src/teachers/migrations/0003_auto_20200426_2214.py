# Generated by Django 2.2.11 on 2020-04-26 22:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200403_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=128, validators=[django.core.validators.RegexValidator(regex='[0-9]*')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(regex='[0-9]*')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(default='2222222', max_length=20),
        ),
    ]