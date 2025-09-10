from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(default=0)
    category = models.CharField(max_length=200)
    description= models.TextField()
    image = models.CharField(max_length=300)

# Add this field to your existing Order model

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow null
    items = models.CharField(max_length=1000)
    total_order = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'product')  # One cart item per user per product
    
    def __str__(self):
        return f"{self.user.username} - {self.product.title} ({self.quantity})"
    
    @property
    def total_price(self):
        return self.quantity * self.product.discount_price