from django.db import models
from django import forms

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"