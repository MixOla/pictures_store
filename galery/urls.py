from django.urls import path

from galery import views

urlpatterns = [
    path('list', views.GaleryListView.as_view(), name='galery_list'),
    ]