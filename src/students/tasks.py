from celery import shared_task



# @shared_task
# def django_sleep(num=5):
#     from time import sleep
#     print('START')
#     sleep(5)
#     print('END')

@shared_task
def logger_list(path='/eee/', method='XXX', time_delta=66):
    # from datetime import datetime, timedelta
    from teachers.models import Logger
    Logger.objects.create(path=path, method=method, time_delta=str(time_delta))
    # Logger.objects.filter(created__lt=datetime.now() - timedelta(days=2)).delete()


@shared_task
def beat():
    from datetime import datetime, timedelta
    from teachers.models import Logger
    # Logger.objects.create(path=path, method=method, time_delta=str(time_delta))
    # Logger.objects.filter(created__lt=datetime.now() - timedelta(days=2)).delete()

    Logger.objects.filter(created__lt=datetime.now() - timedelta(days=7)).delete()

    print('$$$$$$$$$$$$$$$$$$$' * 10)


    # l = Logger.objects.last()
    # print('logger   ', l.time_delta)
