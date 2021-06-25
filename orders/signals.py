from django.db.models.signals import post_save

from orders.models import OrderModel
from paymeuz.models import PaymeTransactionModel


# def update_order_status_click(sender, instance, signal, *args, **kwargs):
#     obj = OrderModel.objects.get(pk=instance.merchant_trans_id)
#     print(instance)
#     if instance.status == 'canceled':
#         obj.payment_status = 4
#     elif instance.status == 'finished':
#         obj.payment_status = 3
#     obj.save()


def update_order_status_payme(sender, instance, signal, *args, **kwargs):
    obj = OrderModel.objects.get(pk=instance.order_id)
    print(instance)
    if instance.status == 'canceled':
        obj.payment_status = 4
    elif instance.status == 'success':
        obj.payment_status = 3
    elif instance.status == 'failed':
        obj.payment_status = 2
    obj.save()


# post_save.connect(update_order_status_click, sender=ClickTransaction, dispatch_uid='update_order_status_click')
post_save.connect(update_order_status_payme, sender=PaymeTransactionModel, dispatch_uid='update_order_status_payme')
