
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from teachers.models import Teacher

@receiver(pre_save, sender=Teacher)
def teacher_pre_save(sender, instance, **kwargs):
    # print(instance.phone)
    phone = ''.join(char for char in instance.phone if char.isdigit())
    instance.phone = phone
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()
    # print(instance.phone)

@receiver(post_save, sender=Teacher)
def teacher_post_save(sender, instance, **kwargs):
    print('post_save\n' * 10)