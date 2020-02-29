from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from users.forms import LoginForm


class LoginView(View):
    """users application LoginView class

    Inherit             : View
    Templates name      : users/login.html
    """

    def get(self, request):
        form = LoginForm()

        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)

                return redirect(reverse("core:home"))

        return render(request, "users/login.html", {"form": form})

