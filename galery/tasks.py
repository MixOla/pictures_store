from celery import shared_task


@shared_task
def print_word(word):
    print("Hello")
