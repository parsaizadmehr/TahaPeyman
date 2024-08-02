from django.db import models

from django.db import models

class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=45)
    category_type = models.CharField(max_length=45)

class Product(models.Model):
    product_name = models.CharField(max_length=20)
    inventory = models.CharField(max_length=10)
    product_code = models.CharField(max_length=10)
    unit_price = models.CharField(max_length=10)
    equipment_price = models.CharField(max_length=10)
    installation_cost = models.CharField(max_length=10)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
