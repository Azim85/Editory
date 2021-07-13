from django.urls import path
from .views import (UserRegisterView, UserLoginView, UserLogoutView,
                    DasboardView, ProfileChange, ChangeStatusView, ChangeStatusCashView, check_payment)

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('dashboard/', DasboardView.as_view(), name='dashboard'),
    path('profile_change/<int:pk>/', ProfileChange.as_view(), name='profile_change'),
    path('change_status/<int:id>/', ChangeStatusView.as_view(), name='change_status'),
    path('change_status_cash/<int:id>/', ChangeStatusCashView.as_view(), name='change_status_cash'),
    path('check/<int:pk>/', check_payment, name='check'),
]