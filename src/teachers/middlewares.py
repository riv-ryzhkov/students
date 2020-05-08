from time import time
from teachers.models import Logger, Teacher, Log
from students_app.models import Student
from groupes.models import Groupe
import teachers.models
from django.db import models
from students.tasks import logger_list

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # t = log(request)

        if request.path.startswith('/admin/'):

            # print(request.path, '!!!!!!!!!!' * 10)
            # teachers.models.Logger.objects.path = request.path
            # Student.objects.create(first_name=request.path, last_name=request.method)
            # Groupe.objects.create(name=request.path, head=request.method)
            # Teacher.objects.create(first_name=request.path, last_name=request.method)
            # Log.objects.create(path=request.path, method=request.method)
            # print('student', Student.objects.last())
            # breakpoint()
            # Logger.objects.create(path=request.path, method=request.method, time_delta='5')
            # breakpoint()
            # print('start middleware' * 10)

            start = time()
            response = self.get_response(request)

            # print('$$$$$$$$$$$$$$$$$$' * 10)

            end = time()
            time_delta = end - start
            path_ = request.path
            method_ = request.method
            time_d_ = str(time_delta)

            # Logger.objects.create(path=request.path, method=request.method, time_delta=str(time_delta))
            # logger_list.delay(request, time_delta)

            logger_list.delay(path=path_, method=method_, time_delta=time_d_)

            # breakpoint()

            # logger_list.delay(r=request, time_delta=time_d_)
            # print('logger' * 40, Log.objects.last())
            # print(type(Student))
            # print(type(Logger))
            # print('end middleware' * 10)
            # return (end - start)
            # print(end - start)
        else:
            response = self.get_response(request)

        # breakpoint()
        # Code to be executed for each request/response after
        # the view is called.

        return response