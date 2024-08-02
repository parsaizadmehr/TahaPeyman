from django.db import models

class Payment(models.Model):
    customer_id = models.PositiveIntegerField()
    payment_number = models.CharField(max_length=10)
    payment_date = models.DateField()
    status = models.CharField(max_length=10)
