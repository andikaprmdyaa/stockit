from django.db import models

class Product(models.Model):
    FASHION = 'Fashion'
    ELECTRONIC = 'Electronic'
    HEALTH_PRODUCT = 'Health Product'
    
    CATEGORY_CHOICES = [
        (FASHION, 'Fashion'),
        (ELECTRONIC, 'Electronic'),
        (HEALTH_PRODUCT, 'Health Product'),
    ]

    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    price = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255)
