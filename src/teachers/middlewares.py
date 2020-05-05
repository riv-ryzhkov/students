from time import time
from teachers.models import Logger
# import teachers.models
# from django.db import models

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # t = log(request)

        if request.path.startswith('/admin/'):
            print(request.path, '7695976596756759659675965')

            # teachers.models.Logger.objects.path = request.path

            # breakpoint()
            print('start middleware')
            print(self)
            start = time()
            response = self.get_response(request)
            end = time()
            Logger.time_delta = end - start
            print(Logger)
            print('end middleware')
            # return (end - start)
            print(end - start)
        else:
            response = self.get_response(request)

        breakpoint()
        # Code to be executed for each request/response after
        # the view is called.

        return response