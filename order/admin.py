from django.contrib import admin

# Register your models here.
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('fcuser', 'product',)


admin.site.register(Order, OrderAdmin)