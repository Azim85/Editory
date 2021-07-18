from django.urls import path
from .views import AboutChangeView


app_name = 'setpage'

urlpatterns = [
    path('', AboutChangeView.as_view(), name='about-change')
]