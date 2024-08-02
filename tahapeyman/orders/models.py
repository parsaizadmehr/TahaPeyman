from django.db import models
from products.models import Product

class Order(models.Model):
    order_number = models.CharField(max_length=20)
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20)
    total_price = models.CharField(max_length=10)
    customer_id = models.AutoField(primary_key=True)
    shipping_info = models.CharField(max_length=45)
    status = models.CharField(max_length=10)

class OrderDetails(models.Model):
    customer_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_number = models.CharField(max_length=10)