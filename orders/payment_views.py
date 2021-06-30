from paymeuz.methods import Paymeuz
from paymeuz.views import MerchantAPIView
from paymeuz import keywords as payme

from orders.models import OrderModel


class CheckOrderPayme(Paymeuz):

    def check_order(self, amount, order_id):
        if order_id:
            exists = OrderModel.objects.filter(pk=order_id).exists()
            if exists:
                obj = OrderModel.objects.get(pk=order_id)
                if amount == obj.amount * 100:
                    return payme.ORDER_FOUND
                return payme.INVALID_AMOUNT
        return payme.ORDER_NOT_FOUND


class PaymeCallbackView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrderPayme
