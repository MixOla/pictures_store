from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass

    def get_absolute_url(self):
        return reverse("galery_detail", kwargs={"img_id": self.pk})

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
