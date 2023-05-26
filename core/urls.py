from django.urls import path

from core import views

urlpatterns = [
    path("logout", views.logout_user, name="logout"),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
]
