from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from .forms import LoginForm, UserRegistrationForm




def logout_user(request):
    logout(request)
    return redirect("galery_list")


class RegisterUser(View):
    form_class = UserRegistrationForm
    template_name = 'galery/register.html'
    success_url = reverse_lazy('generate_image')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"user_form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data["password"])
            # Save the User object
            new_user.save()
            return redirect('login')
        return render(request, self.template_name, {"user_form": form})


class LoginUser(View):
    form_class = LoginForm
    template_name = 'galery/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                request, username=cleaned_data["username"], password=cleaned_data["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("galery_list")
                return HttpResponse("Отключенная учетная запись")
            else:
                return HttpResponse("Недопустимый логин")
        return render(request, self.template_name, {"form": form})

    def get_success_url(self):
        return reverse_lazy('home')
