# Generated by Django 4.2.1 on 2023-05-25 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("galery", "0004_rename_imgs_galery_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="galery",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="galery",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]
