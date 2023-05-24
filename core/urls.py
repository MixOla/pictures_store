from django.urls import path

from core import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
]