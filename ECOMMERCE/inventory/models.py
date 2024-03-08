import uuid

from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name=models.CharField(
        max_length=100,
        verbose_name="First Name",
        help_text="Enter name of inventory category"
        )
    slug=models.SlugField(unique=True,null=True,blank=True)
    is_active=models.BooleanField()
    parent=models.ForeignKey('self',on_delete=models.PROTECT,null=True,blank=True)

    class Meta:
        verbose_name="Inventory Category"
        verbose_name_plural="Categories"
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.name


class SeasonalEvents(models.Model):
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    name=models.CharField(max_length=100,unique=True)


class ProductType(models.Model):
    name=models.CharField(max_length=100)
    parent=models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    IN_STOCK="IS"
    OUT_OF_STOCK="OOS"
    BACK_ORDERED="BO"

    STOCK_STATUS={
    IN_STOCK : "In Stock",
    OUT_OF_STOCK : "Out of stock",
    BACK_ORDERED : "Back Ordered",
    }
    pid=models.CharField(max_length=255)
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    description=models.TextField(null=True)
    is_digital=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True, editable=False)
    updated_at=models.DateTimeField(auto_now=True,editable=False)
    is_active=models.BooleanField(default=False)
    stock_status=models.CharField(
        max_length=3,
        choices=STOCK_STATUS,
        default=OUT_OF_STOCK
        )
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    seasonal_event=models.ForeignKey(SeasonalEvents,on_delete=models.SET_NULL,null=True,blank=True)
    product_type=models.ManyToManyField(ProductType,related_name="product_type")

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True)
    text=models.CharField(max_length=100,default="asdf;lkj",null=True)


class AttributeValue(models.Model):
    attribute_value=models.CharField(max_length=100)
    attribute=models.ForeignKey(Attribute,on_delete=models.CASCADE)


class ProductLine(models.Model):
    price=models.DecimalField(decimal_places=2, max_digits=5)
    sku=models.UUIDField(default=uuid.uuid4)
    stock_qty=models.IntegerField(default=0)
    is_active=models.BooleanField(default=False)
    order=models.IntegerField()
    weight=models.FloatField()
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    attribute_values=models.ManyToManyField(AttributeValue,related_name="attribute_values")

class ProductImage(models.Model):
    name=models.CharField(max_length=100)
    alternative_text=models.CharField(max_length=100)
    url=models.ImageField()
    order=models.IntegerField()
    product_line=models.ForeignKey(ProductLine,on_delete=models.CASCADE)


class ProductLine_AttributeValue(models.Model):
    attribute_value=models.ForeignKey(AttributeValue,on_delete=models.CASCADE)
    product_line=models.ForeignKey(ProductLine,on_delete=models.CASCADE)


class Product_ProductType(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_type=models.ForeignKey(ProductType,on_delete=models.CASCADE)

    