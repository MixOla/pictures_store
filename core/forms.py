
from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data["password"] != cleaned_data["password2"]:
            raise forms.ValidationError("Введенные пароли не совпадают")
        return cleaned_data["password2"]
