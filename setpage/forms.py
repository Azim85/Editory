from django import forms
from .models import AboutUsModel, WebinarsModel, TranslationModel


class AboutUSForm(forms.ModelForm):
    class Meta:
        model = AboutUsModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text6_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text6_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text6_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }


class TranslationsForm(forms.ModelForm):
    class Meta:
        model = TranslationModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_en': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_ru': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_uz': forms.TextInput(attrs={'class': 'form-control'}),
        }


class WebinarsForm(forms.ModelForm):
    class Meta:
        model = WebinarsModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }