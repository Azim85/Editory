from django.urls import path

from orders.views import OrderCreateView, OrderCancelView, order_export, CreateOrderView

app_name='orders'

urlpatterns = [
    path('create', OrderCreateView.as_view(),  name='create'),
    path('cancel/<int:pk>', OrderCancelView.as_view(), name='cancel'),
    path('export', order_export, name='export'),
    path('create_order/', CreateOrderView.as_view(), name="create-order")
]
