from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.HomePageView.as_view(), name="galery_list"),
    path("generate-image/", views.GaleryGenerateImage.as_view(), name="generate_image"),
    path("user-image/", views.UserGaleryImageView.as_view(), name="user_image"),
]
