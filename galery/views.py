from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView

from galery.forms import NewImageForm
from galery.models import Galery
from galery.tasks import generate_image


class HomePageView(TemplateView):
    template_name = "galery/home.html"


class GaleryGenerateImage(LoginRequiredMixin, TemplateView):
    form_class = NewImageForm
    template_name = "galery/generate_picture.html"
    success_url = reverse_lazy('generate_picture')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('generate_picture')
        return render(request, self.template_name, {"form": form})


    def form_valid(self, form):
        generate_image.delay(
            description=form.cleaned_data["prompt"], user_id=self.request.user.id
        )
        return super().form_valid(form)


class UserGaleryImageView(ListView):
    model = Galery
    template_name = "galery/user_page.html"
    success_url = reverse_lazy('user-image')

    def get_context_data(self, **kwargs):
        queryset = Galery.objects.filter(user=self.request.user)
        return {
            'img': queryset
        }
