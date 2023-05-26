from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormView
from rest_framework import permissions

from core.models import User
from galery.forms import NewImageForm
from galery.models import Galery
from galery.tasks import generate_image


class GaleryListView(ListView):
    model = Galery
    queryset = Galery.objects.all()
    permission_classes = [permissions.AllowAny]

    def show_all_pictures(request):
        pictures = Galery.objects.all()
        if request.user:
            pictures = pictures.filter(user=request.user.id)
        else:
            users = User.objects.filter(is_superuser=True)
            if users:
                pictures = pictures.filter(user__in=users)
            else:
                pictures = []
        return render(request, "galery/home.html", {"pictures": pictures})



class GaleryGenerateImage(LoginRequiredMixin, FormView):
    form_class = NewImageForm
    template_name = "galery/generate_picture.html"


    def get_success_url(self):
        return reverse('user_image')

    def show_form(self, request):
        return render(request, "galery/generate_picture.html")

    def form_valid(self, form):
        generate_image.delay(
            description=form.cleaned_data["prompt"], user_id=self.request.user.id
        )
        return super().form_valid(form)


class UserGaleryImageView(FormView):
    template_name = "galery/user_page.html"

    def get_context_data(self, **kwargs):
        queryset = Galery.objects.filter(user=self.request.user)
        return {
            'images': queryset
        }