from rest_framework import serializers

from core.serializers import UserSerializer
from galery.models import Galery


class GalerySerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Galery
        fields = ['id', 'img', 'prompt']
        # read_only_fields = '__all__'
#