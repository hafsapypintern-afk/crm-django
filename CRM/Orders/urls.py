from django.urls import path
from . import views

urlpatterns = [
    path("", views.order_list, name="order_list"),
    path("add_order/", views.add_order, name="add_order"),
    path("<int:id>/", views.order_detail, name="order_detail"),
    path("<int:id>/update_order/", views.update_order, name="update_order"),
    path("<int:id>/delete_order/", views.delete_order, name="delete_order"),
]