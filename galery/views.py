from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from rest_framework import permissions


from core.models import User
from galery.forms import NewImageForm
from galery.models import Galery
from galery.serializers import GalerySerializer
from galery.tasks import print_word


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
        return render(request, 'galery/home.html', {
            'pictures': pictures
        })



class GaleryGenerateImage(FormView):
    form_class = NewImageForm
    template_name = 'galery/generate_picture.html'
    # model = Galery
    # queryset = Galery.objects.all()
    # serializer_class = GalerySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def show_form(request):
        return render(request, 'galery/generate_picture.html')

    def form_valid(self, form):
        print(form)
        task.hjhgj.delay(form.data)
        return super().form_valid(form)
