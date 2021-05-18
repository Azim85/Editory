from django import forms
from django.forms import widgets
from .models import Consultation
from .models import ApplicationForFreeConsultation
import re


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


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if ('998' not in phone) or len(phone)>11:
            raise forms.ValidationError('номер неправильного формата')
        return phone

    def clean_organization_contacts(self):
        phone = self.cleaned_data.get('organization_contacts')
        if ('998' not in phone) or len(phone)>11:
            raise forms.ValidationError('номер неправильного формата')
        return phone


BUSYNESS = (
    ('student', 'student'),
    ('busy', 'busy'),
)

class FreeConsultationForm(forms.ModelForm):

    busyness = forms.ChoiceField(choices=BUSYNESS, widget=forms.RadioSelect(attrs={'class':''}))

    class Meta:
        model = ApplicationForFreeConsultation
        fields = "__all__"


        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }