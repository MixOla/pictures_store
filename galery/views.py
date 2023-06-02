from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView

from galery.forms import NewImageForm
from galery.models import Galery
from galery.tasks import generate_image


class HomePageView(TemplateView):
    template_name = "galery/home.html"


class GaleryGenerateImage(LoginRequiredMixin, TemplateView):
    form_class = NewImageForm
    template_name = "galery/generate_picture.html"

    def get_success_url(self):
        return reverse('generate_image')

    def form_valid(self, form):
        generate_image.delay(
            description=form.cleaned_data["prompt"], user_id=self.request.user.id
        )
        return super().form_valid(form)


class UserGaleryImageView(TemplateView):
    template_name = "galery/user_page.html"

    def get_context_data(self, **kwargs):
        queryset = Galery.objects.filter(user=self.request.user)
        return {
            'images': queryset
        }
