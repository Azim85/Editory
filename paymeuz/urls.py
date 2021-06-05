from django.urls import path
from orders.payment_views import PaymeCallbackView

urlpatterns = [
    # path('click/transaction/', ClickCallbackView.as_view()),
    path('payme/transaction/', PaymeCallbackView.as_view()),
]

