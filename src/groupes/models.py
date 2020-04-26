from django.db import models

class Groupe(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    head = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, default='')
    head_teach = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, related_name='groups')


    def info(self):
        return f'{self.id} {self.name} {self.head} {self.email} {self.phone} {self.head_teach}'

    def __str__(self):
        return f'{self.name}  Boss - {self.head_teach}'
