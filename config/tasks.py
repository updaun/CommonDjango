from celery import shared_task


@shared_task
def calculate_sum(a, b):
    return a + b
