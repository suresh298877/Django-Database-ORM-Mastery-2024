from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    IN_STOCK="IS"
    OUT_OF_STOCK="OOS"
    BACKORDERED="BO"

    STOCK_STATUS={
    IN_STOCK : "In Stock",
    OUT_OF_STOCK : "Out of stock",
    BACKORDERED : "Back Ordered",
    }
    pid=models.CharField(max_length=255)
    name=models.CharField(max_length=100)
    slug=models.SlugField()
    description=models.TextField()
    is_digital=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True, editable=False)
    updated_at=models.DateTimeField(auto_now_add=False,editable=False)
    is_active=models.BooleanField()
    stock_status=models.CharField(
        max_length=3,
        choices=STOCK_STATUS,
        default=OUT_OF_STOCK
        )

class ProductLine(models.Model):
    price=models.DecimalField()
    sku=models.UUIDField(default=uuid.uuid4)
    stock_qty=models.IntegerField()
    is_active=models.BooleanField()
    order=models.IntegerField()
    weight=models.FloatField()

class ProductImage(models.Model):
    name=models.CharField(max_length=100)
    alternative_text=models.CharField(max_length=100)
    url=models.ImageField()
    order=models.IntegerField()

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField()
    is_active=models.BooleanField()

class SeasonalEvents(models.Model):
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    name=models.CharField(max_length=100)
