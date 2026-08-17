from django.urls import path
from . import views

urlpatterns = [
    path("", views.customer_list, name="customer_list"),
    path("add/", views.add_customer, name="add_customer"),
    path("<int:id>/", views.customer_detail, name="customer_detail"),
    path("<int:id>/edit/", views.update_customer, name="update_customer"),
    path("<int:id>/delete/", views.delete_customer, name="delete_customer"),
]