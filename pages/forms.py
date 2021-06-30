from django import forms
from django.forms import widgets
from .models import ResumeModel

class ResumeForm(forms.ModelForm):

    """Resume form for ResumeModel"""

    class Meta:
        model = ResumeModel
        fields = ['first_name', 'last_name', 'profession', 'about_me', 'resume', 'is_agree']

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'profession': forms.TextInput(attrs={'class':'form-control'}),
            'about_me': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
        }