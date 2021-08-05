from django.urls import path

from orders.views import OrderCreateView, OrderCancelView, order_export, CreateOrderView, ChooseTypeView, TransPaymentView, ChangePaymentTypeView

app_name='orders'

urlpatterns = [
    path('create', OrderCreateView.as_view(),  name='create'),
    path('cancel/<int:pk>', OrderCancelView.as_view(), name='cancel'),
    path('export', order_export, name='export'),
    path('create_order/', CreateOrderView.as_view(), name="create-order"),
    path('payment_type/', ChooseTypeView.as_view(), name='choose-type'),
    path('translation_payment/', TransPaymentView.as_view(), name='translation-payment'),
    path('change_payment_type/', ChangePaymentTypeView.as_view(), name='change-payment-type')
]
