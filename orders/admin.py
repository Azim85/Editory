from django.contrib import admin
from .models import OrderModel


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'product', 'amount', 'phone', 'email', 'file', 'payment_type', 'payment_status', 'delivery_status')
    
admin.site.register(OrderModel, OrderAdmin)

