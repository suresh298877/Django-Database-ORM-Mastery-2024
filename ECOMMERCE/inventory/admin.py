from django.contrib import admin

from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields={
#         'slug' : ('name',)
#     }
    list_display=['name','slug','is_active']
    search_fields=['name','slug']


class ProductAdmin(admin.ModelAdmin):
    list_filter=('stock_status',)
admin.site.register(Category,CategoryAdmin)
# admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductType)