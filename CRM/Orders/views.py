from django.shortcuts import redirect, render,get_object_or_404
from .models import Order
from .forms import OrderForm    

# Create your views here .__ = go through a relationship to another field
#filter() :"Give me all matching results."
#get() "Give me the one object I'm looking for."

def order_list(request):
    orders = Order.objects.all()
    return render(
        request, "order_list.html", {"orders": orders}  #Template, I'm giving you the orders data.  You can access it using the name orders."
    )

def add_order(request):

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_list")
    else:
        form = OrderForm()

    return render(request, "add_order.html", {"form": form})

def update_order(request, id):

    order = get_object_or_404(Order, id=id)

    if request.method == "POST":

        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect("order_list")

    else:
        form = OrderForm(instance=order)

    return render(request, "update_order.html",
        {
            "form": form,
            "order": order
        }
    )

def delete_order(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        order.delete()
        return redirect("order_list")

    return render(request,"delete_order.html", {"order": order})

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)

    return render(
        request, "order_detail.html", {"order": order})
