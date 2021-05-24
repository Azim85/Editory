from django import forms
import re
from .models import Consultation, ApplicationForFreeConsultation



class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('first_name', 'last_name', 'phone', 'comment')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows':7}),
        }

    
    def clean_phone(self):
        phone_len = [12, 13]
        phone = self.cleaned_data.get('phone')
        if '+998'  or '998' in phone:
            if len(phone) in phone_len:
                return phone
        raise forms.ValidationError('неправильный формат номера телефона')
        


BUSYNESS = (
    ('student', 'student'),
    ('busy', 'busy')
)
DEGREE = (
    ('кандидат наук', 'кандидат наук '),
    ('доктор наук', 'доктор  наук'),
    ('доктор философии', 'доктор философии PhD'),
    ('хабилитированный доктор', 'хабилитированный доктор (Dr. habil.)'),
)

class FreeConsultationForm(forms.ModelForm):
    busyness = forms.ChoiceField(choices=BUSYNESS, widget=forms.RadioSelect())
    academic_degree = forms.ChoiceField(choices=DEGREE, widget=forms.Select(attrs={'class':'form-control'}))
    upload_file = forms.ImageField(help_text='kkkkkkk')

    class Meta:
        model = ApplicationForFreeConsultation
        fields = '__all__'

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'place_of_work' : forms.TextInput(attrs={'class':'form-control'}),
            'application_name' : forms.TextInput(attrs={'class':'form-control'}),
            'conference' : forms.TextInput(attrs={'class':'form-control'}),
            'section' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_first_name(self):
        firstname = self.cleaned_data.get('first_name')
        if firstname != 'Azim':
            raise forms.ValidationError('poof')
        return firstname

    def clean_phone(self):
        phone_len = [10, 11]
        phone = self.cleaned_data.get('phone')
        if '+998'  or '998' in phone:
            if len(phone) in phone_len:
                return phone
        raise forms.ValidationError('неправильный формат номера телефона')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError('электронная почта недействительна')
        return email
