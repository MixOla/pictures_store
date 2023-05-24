from django.db import models
from django.urls import reverse


class Galery(models.Model):
    prompt = models.TextField(verbose_name='Описание', null=True, blank=True)
    img = models.ImageField()
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    user = models.ForeignKey(
        'core.User',
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="user",
    )

    def get_absolute_url(self):
        return reverse('galery_detail', kwargs={'img_id': self.pk})

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
        # ordering = ['-created']


    def __str__(self):
        return self.prompt

