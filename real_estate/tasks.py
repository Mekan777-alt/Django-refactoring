from celery import shared_task
from time import sleep


@shared_task
def generate_rental_agr(lease):
    # Какая-то очень долгая логика по генерации документа
    sleep(20)
