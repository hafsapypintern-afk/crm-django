from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm


def customer_list(request):
    customers = Customer.objects.all()

    return render(
        request,
        "customers/customer_list.html",
        {"customers": customers}
    )


def add_customer(request):

    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("customer_list")

    else:
        form = CustomerForm()

    return render(
        request,
        "customers/add_customer.html",
        {"form": form}  #Send this CustomerForm object to the template under the name form
    )

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)

    return render(
        request,
        "customers/customer_detail.html",
        {"customer": customer}
    )
def update_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect("customer_detail", id=customer.id)

    else:
        form = CustomerForm(instance=customer)

    return render(    #render() = take a template + data → produce a webpage response for the browser.
        request,
        "customers/update_customer.html",
        {"form": form, "customer": customer}
    )

def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")

    return render(
        request,
        "customers/delete_customer.html",
        {"customer": customer}
    )