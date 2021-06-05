from django import forms
from django.forms import fields
from .models import OrderModel

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['phone', 'email', 'file']