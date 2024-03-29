from django.contrib import admin

# Register your models here.
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)


admin.site.register(Product, ProductAdmin)