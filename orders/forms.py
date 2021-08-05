from django import forms
from django.forms import fields, widgets
from django.utils.translation import ugettext_lazy as _
from .models import OrderModel

PAYMENT_TYPES = (
    (3, _('Apelsin')),
    (4, _('Payme')),
)

class OrderForm(forms.ModelForm):
    payment_type = forms.ChoiceField(choices=PAYMENT_TYPES, widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = OrderModel
        fields = ['phone', 'email', 'file', 'payment_type']

        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }

