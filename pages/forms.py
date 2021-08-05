from django import forms
from django.forms import widgets
from .models import ResumeModel, Topic

class ResumeForm(forms.ModelForm):

    """Resume form for ResumeModel"""
    is_agree = forms.BooleanField(error_messages={'required': 'Вы должны согласиться с Правилами и Условиями'})

    class Meta:
        model = ResumeModel
        fields = ['first_name', 'last_name', 'profession', 'about_me', 'resume', 'is_agree']

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'profession': forms.TextInput(attrs={'class':'form-control'}),
            'about_me': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
        }

class TopicForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':6}))
    others = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':6}))
    class Meta:
        model = Topic
        fields = ['main_image', 'material_name', 'title', 'description', 'others', ]

        widgets = {
            'material_name': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # 'description': forms.Textarea(attrs={'class':'form-control', 'rows':6}),
            # 'others': forms.Textarea(attrs={'class':'form-control', 'rows':6}),

        }