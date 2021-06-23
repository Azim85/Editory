from django.urls import path
from .views import *

app_name = 'editorypress'

urlpatterns = [
    path('', HomeView.as_view(), name='main')
]
