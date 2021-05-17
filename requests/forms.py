from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('first_name', 'last_name', 'phone',
                  'material', 'organization', 'organization_contacts', 'address')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'organization_contacts': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
