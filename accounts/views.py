from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LogInForm
from .forms import SignupForm
from django.contrib.auth.models import User


def user_logout(request):
    logout(request)
    return redirect("login")


def user_login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("list_projects")
    else:
        form = LogInForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            if password != password_confirmation:
                error_message = "The passwords do not match"
                return render(
                    request,
                    "registration/signup.html",
                    {"form": form, "error_message": error_message},
                )
            if User.objects.filter(username=username).exists():
                error_message = "The username is already taken"
                return render(
                    request,
                    "registration/signup.html",
                    {"form": form, "error_message": error_message},
                )
            user = User.objects.create_user(
                username=username, password=password
            )
            login(request, user)
            return redirect("list_projects")
    else:
        form = SignupForm()
    context = {
        "form": form,
    }
    return render(request, "registration/signup.html", context)
