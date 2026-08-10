from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def Home(request):
    return render(request, 'Home.html')

def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return redirect("Home")

    return render(request, "Login.html")

def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("Home")

    return render(request, "Register.html")