from django.db import models
from .fields import ProductIdField
class Product(models.Model):
    name = models.CharField(max_length=100)
    productid=ProductIdField()

class Category(models.Model):
    name = models.CharField(max_length=100)