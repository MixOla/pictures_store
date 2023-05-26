import time
from django.contrib.auth import get_user_model
from pictures_store.celery import app
from .handler import GenerateImageHandler
from .models import Galery

User = get_user_model()


@app.task
def generate_image(description: str, user_id: int):
    print(description, user_id)
    handler = GenerateImageHandler()
    order_id: str = handler.initiate_processing(prompt=description)
    print(f"{order_id=}")

    status = None
    while status != "completed":
        if status == "non-existant":
            print("Processing error!")
            break
        time.sleep(10)
        status = handler.check_status(order_id)
        print(f"{status=}")

    result: dict = handler.get_results(order_id)
    user = User.objects.get(id=user_id)
    for raw_image in result["imgs"]:
        img = handler.decode_img(raw_image)
        galery = Galery.objects.create(prompt=description, img=img, user=user)
        print(f"{galery=}")
