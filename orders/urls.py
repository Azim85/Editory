from django.urls import path

from orders.views import OrderCreateView, OrderCancelView, order_export, create_order

urlpatterns = [
    path('create', OrderCreateView.as_view(), name='create'),
    path('cancel/<int:pk>', OrderCancelView.as_view(), name='cancel'),
    path('export', order_export, name='export'),
    path('create_order', create_order, name="create-order")
]
