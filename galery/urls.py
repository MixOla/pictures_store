from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.GaleryListView.show_all_pictures, name='galery_list'),
    path('generate_image/', views.GaleryGenerateImage.as_view(), name='generate_image'),
]


