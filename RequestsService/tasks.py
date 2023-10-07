from celery import shared_task

@shared_task
def your_async_task(arg1, arg2):
    result = arg1 + arg2
    return result
