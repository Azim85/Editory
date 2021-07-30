from django import forms

from .models import WebinarsModel, TranslationModel

from .models import (AboutUsModel, BakModel, ConferencesModel, ContactModel, CreateConferenceModel,
                     DesignModel, GrantsModel, PatentModel, ScopusModel, ProofModel, LangEditModel)


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
            #
            # 'text1_en': forms.TextInput(attrs={'class':'form-control'}),
            # 'text2_en': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            # 'text3_en': forms.TextInput(attrs={'class':'form-control'}),
            # 'text4_en': forms.TextInput(attrs={'class':'form-control'}),
            # 'text5_en': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            # 'text6_en': forms.TextInput(attrs={'class':'form-control'}),
            # 'text7_en': forms.TextInput(attrs={'class':'form-control'}),
            # 'text8_en': forms.TextInput(attrs={'class':'form-control'}),
            # 'text9_en': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            # 'text10_en': forms.TextInput(attrs={'class':'form-control'}),
            # 'text11_en': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            #
            # 'text1_ru': forms.TextInput(attrs={'class':'form-control'}),
            # 'text2_ru': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            # 'text3_ru': forms.TextInput(attrs={'class':'form-control'}),
            # 'text4_ru': forms.TextInput(attrs={'class':'form-control'}),
            # 'text5_ru': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            # 'text6_ru': forms.TextInput(attrs={'class':'form-control'}),
            # 'text7_ru': forms.TextInput(attrs={'class':'form-control'}),
            # 'text8_ru': forms.TextInput(attrs={'class':'form-control'}),
            # 'text9_ru': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            # 'text10_ru': forms.TextInput(attrs={'class':'form-control'}),
            # 'text11_ru': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            #
            # 'text1_uz': forms.TextInput(attrs={'class':'form-control'}),
            # 'text2_uz': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            # 'text3_uz': forms.TextInput(attrs={'class':'form-control'}),
            # 'text4_uz': forms.TextInput(attrs={'class':'form-control'}),
            # 'text5_uz': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            # 'text6_uz': forms.TextInput(attrs={'class':'form-control'}),
            # 'text7_uz': forms.TextInput(attrs={'class':'form-control'}),
            # 'text8_uz': forms.TextInput(attrs={'class':'form-control'}),
            # 'text9_uz': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            # 'text10_uz': forms.TextInput(attrs={'class':'form-control'}),
            # 'text11_uz': forms.Textarea(attrs={'class':'form-control', 'rows':5})
        }


class BakForm(forms.ModelForm):
    class Meta:
        model = BakModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text16_en': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text16_ru': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text16_uz': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ConferencesForm(forms.ModelForm):
    class Meta:
        model = ConferencesModel
        fields = '__all__'

        widgets = {

            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_link_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text6_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_link_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text8_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_link_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_link_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text12_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_link_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text14_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_link_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text16_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text17_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_link_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text6_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_link_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text8_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_link_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_link_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text12_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_link_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text14_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_link_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text16_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text17_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_link_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text6_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_link_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text8_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_link_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_link_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text12_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_link_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text14_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_link_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text16_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text17_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

        widgets = {
            'text1': forms.TextInput(attrs={'class': 'form-control'}),
            'text2': forms.TextInput(attrs={'class': 'form-control'}),
            'text3': forms.TextInput(attrs={'class': 'form-control'}),
            'text4': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_uz': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreateConferenceForm(forms.ModelForm):
    class Meta:
        model = CreateConferenceModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control'}),
        }


class DesignForm(forms.ModelForm):
    class Meta:
        model = DesignModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text7_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text7_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text7_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class GrantForm(forms.ModelForm):
    class Meta:
        model = GrantsModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class PatentForm(forms.ModelForm):
    class Meta:
        model = PatentModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text5_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text6_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text11_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text5_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text6_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text11_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text4_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text5_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text6_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text11_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class ScopusForm(forms.ModelForm):
    class Meta:
        model = ScopusModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text5_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text7_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text9_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text16_en': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text5_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text7_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text9_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text16_ru': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text5_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text7_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text9_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text10_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text16_uz': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProofForm(forms.ModelForm):
    class Meta:
        model = ProofModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text5_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text7_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text9_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_en': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text5_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text7_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text9_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_ru': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text5_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text7_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text9_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_uz': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LangForm(forms.ModelForm):
    class Meta:
        model = LangEditModel
        fields = '__all__'

        widgets = {
            'text1_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text2_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text16_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text17_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text18_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text19_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text20_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text21_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text22_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text23_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text24_en': forms.TextInput(attrs={'class': 'form-control'}),
            'text25_en': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text2_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text16_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text17_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text18_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text19_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text20_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text21_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text22_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text23_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text24_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'text25_ru': forms.TextInput(attrs={'class': 'form-control'}),

            'text1_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text2_uz': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'text3_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text4_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text5_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text6_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text7_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text8_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text9_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text10_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text11_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text12_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text13_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text14_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text15_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text16_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text17_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text18_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text19_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text20_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text21_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text22_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text23_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text24_uz': forms.TextInput(attrs={'class': 'form-control'}),
            'text25_uz': forms.TextInput(attrs={'class': 'form-control'}),

        }
