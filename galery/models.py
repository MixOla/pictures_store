from django.db import models
from django.urls import reverse


def upload_to_galery(instance: "Galery", filename: str):
    return f"gallery/{instance.user_id}/{filename}"


class Galery(models.Model):
    prompt = models.TextField(verbose_name="Описание", null=True, blank=True)
    img = models.ImageField(upload_to=upload_to_galery)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    user = models.ForeignKey(
        "core.User",
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="galery",
    )

    def get_absolute_url(self):
        return reverse("galery_detail", kwargs={"img_id": self.pk})

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"


# def upload_to_galery(instance: "Galery", filename: str):
#     return f"gallery/{instance.user_id}/{filename}"
#
# class Picture(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     img = models.ImageField(upload_to=upload_to_galery)
#     created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
#     user = models.ForeignKey(
#         "core.User",
#         verbose_name="Пользователь",
#         on_delete=models.CASCADE,
#         related_name="picture",
#     )
#
# class Galery(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     prompt = models.TextField(verbose_name="Описание", null=True, blank=True)
#     img = models.ForeignKey(
#         "Picture",
#         verbose_name="Изображение",
#         on_delete=models.CASCADE,
#         related_name="galery",
#         )
#     user = models.ForeignKey(
#         "core.User",
#         verbose_name="Пользователь",
#         on_delete=models.CASCADE,
#         related_name="galery",
#     )
#
#     def get_absolute_url(self):
#         return reverse("galery_detail", kwargs={"img_id": self.pk})
#
#     class Meta:
#         verbose_name = "Картинка"
#         verbose_name_plural = "Картинки"
#
#
#
