from django import forms
from .models import Consultation, ApplicationForFreeConsultation


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