from django.db import models
from customers.models import Customer

# Create your models here.Create a field called customer that creates a 
# foreign-key relationship to the Customer model. 
# If that Customer is deleted, delete the related Order as well

class Order (models.Model):
    customer= models.ForeignKey (Customer, on_delete = models.CASCADE)
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add= True)

