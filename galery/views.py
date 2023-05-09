from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView

from galery.models import Galery
from galery.serializers import GalerySerializer


class GaleryListView(ListAPIView):
    model = Galery
    queryset = Galery.objects.all()
    serializer_class = GalerySerializer
    permission_classes = [permissions.AllowAny]


    # return render(request, 'galery/base.html', {'title': 'Главная страница'})