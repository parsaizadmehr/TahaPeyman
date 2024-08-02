from django.db import models

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    virtual_number = models.CharField(max_length=100)
    subject_text = models.CharField(max_length=100)
    text = models.TextField()
