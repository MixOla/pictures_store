# from django.db import models
#
# class Picture(models.Model):
#     description = models.TextField(verbose_name='Описание', null=True, blank=True)
#     created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
#     user = models.ForeignKey(
#         'core.User',
#         verbose_name="Пользователь",
#         on_delete=models.CASCADE,
#         related_name="user",
#     )
#
#     class Meta:
#         verbose_name = "Картинка"
#         verbose_name_plural = "Картинки"
#
#     def __str__(self):
#         return self.description