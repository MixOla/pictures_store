from django.contrib.auth import get_user_model
from django.forms import Form
from django import forms

from core.models import User
from galery.models import Galery

User = get_user_model()


class NewImageForm(Form):
    prompt = forms.CharField(label='prompt', widget=forms.Textarea())

    class Meta:
        model = Galery
        fields = ('prompt',)
