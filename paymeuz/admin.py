from django.contrib import admin
from .models import PaymeTransactionModel


class PaymeTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', '_id', 'request_id', 'amount', 'order_id', 'state', 'status', 'date')
    list_display_links = ('id',)
    list_filter = ('status',)
    search_fields = ('request_id', 'status', 'id', '_id')


admin.site.register(PaymeTransactionModel, PaymeTransactionAdmin)
