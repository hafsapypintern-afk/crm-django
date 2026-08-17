from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from customers.models import Customer
from Orders.models import Order
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request, 'Home.html')

@login_required
def Dashboard(request):
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status="Pending").count()

    recent_customers = Customer.objects.order_by("-created_at")[:5]
    recent_orders = Order.objects.select_related("customer").order_by("-created_at")[:5]

    return render(request, "Dashboard.html", {
        "total_customers": total_customers,
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "recent_customers": recent_customers,
        "recent_orders": recent_orders,
    })

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

            return redirect("Dashboard")

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

def logout_view(request):
    logout(request)
    return redirect("Home")