from django.core.management.base import BaseCommand
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Clean phone!!!'

    def handle(self, *args, **options):
        # 100,000,000
        for teacher in Teacher.objects.exclude(phone='').iterator():
            # 1
            # phone = ''
            # for char in student.phone:
            #     if char.isdigit():
            #         phone += char
            ##########################
            # phone = ''.join([char for char in student.phone if char.isdigit()])
            phone = ''.join(char for char in teacher.phone if char.isdigit())
            # phone = ''.join(filter(lambda x: x.isdigit(), student.phone))
            teacher.phone = phone
            teacher.save()


# [i for i in range(10)]
# (i for i in range(10))