from django.db import models

class item(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount= models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    location = models.TextField()