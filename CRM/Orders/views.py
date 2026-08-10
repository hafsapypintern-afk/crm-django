from django.shortcuts import render
from .models import Order

# Create your views here .__ = go through a relationship to another field
#filter() :"Give me all matching results."
#get() "Give me the one object I'm looking for."

def Order_list(request):
    orders= Order.objects.all()
    return render(request, 'Orders/order_list.html', {'orders': orders})