from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, validate_integer, RegexValidator
import re


class Teacher(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, validators=[RegexValidator(regex='[0-9]*')])
    email = models.EmailField(max_length=128, validators=[RegexValidator(regex='[0-9]*')])
    age = models.IntegerField(null=True, default=None, validators=[MinValueValidator(18), MaxValueValidator(100)])
    phone = models.CharField(max_length=20, default='2222222')



    def info(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.email} {self.phone}'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
