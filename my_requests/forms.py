from django import forms
import re
from django.forms import widgets
from .models import (   Consultation, 
                        ApplicationForFreeConsultation, 
                        OrganizeResearches, 
                        Proofreading,
                        PeerReview,
                        OrganizeConferences,
                        Grants,
                        Translation
                    )


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('first_name', 'last_name', 'phone',  'is_agree')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    
    def clean_phone(self):
        phone_len = [12, 13]
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
    upload_file = forms.FileField()

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


    def clean_phone(self):
        phone_len = [12, 13]
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


class OrganizeResearchForm(forms.ModelForm):

    is_agree = forms.BooleanField(error_messages={'required': 'Вы должны согласиться с Правилами и Условиями'})
    class Meta:
        model = OrganizeResearches
        fields = '__all__'

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'select_topic' : forms.Select(attrs={'class':'form-control'}),
            'organization' : forms.TextInput(attrs={'class':'form-control'}),
            'org_contacts' : forms.TextInput(attrs={'class':'form-control'}),
            'org_address' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_phone(self):
        phone_len = [12, 13]
        phone = self.cleaned_data.get('phone')
        if '+998'  or '998' in phone:
            if len(phone) in phone_len:
                return phone
        raise forms.ValidationError('неправильный формат номера телефона')

    def clean_org_contacts(self):
        phone_len = [12, 13]
        org_contacts = self.cleaned_data.get('org_contacts')
        if '+998'  or '998' in org_contacts:
            if len(org_contacts) in phone_len:
                return org_contacts
        raise forms.ValidationError('неправильный формат номера телефона')

class ProofreadingForm(forms.ModelForm):
    upload_file = forms.FileField()
    is_agree = forms.BooleanField(error_messages={'required': 'Вы должны согласиться с Правилами и Условиями'})
    class Meta:
        model = Proofreading
        fields = '__all__'

        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'material_name':forms.TextInput(attrs={'class':'form-control'}),
            'research_area':forms.TextInput(attrs={'class':'form-control'}),
            'choose':forms.Select(attrs={'class':'form-control'}),
            'word_count':forms.NumberInput(attrs={'min': '0', 'class': 'form-control'}),
            'language_editing':forms.TextInput(attrs={'class':'form-control'}),
            'certificate':forms.Textarea(attrs={'class':'form-control', 'rows':4}),
            'comment':forms.Textarea(attrs={'class':'form-control', 'rows':5}),
        }

class PeerReviewForm(forms.ModelForm):
    upload_file = forms.FileField()
    is_agree = forms.BooleanField(error_messages={'required': 'Вы должны согласиться с Правилами и Условиями'})
    class Meta:
        model = PeerReview
        fields = '__all__'

        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'material_name':forms.TextInput(attrs={'class':'form-control'}),
            'research_area':forms.TextInput(attrs={'class':'form-control'}),
            'choose':forms.Select(attrs={'class':'form-control'}),
            'academic_degree':forms.TextInput(attrs={'class':'form-control'}),
            'organization':forms.TextInput(attrs={'class':'form-control'}),
            'scientific_adviser':forms.TextInput(attrs={'class':'form-control'}),
            'comment':forms.Textarea(attrs={'class':'form-control', 'rows':5}),
        }


class OrganizeConferencesForm(forms.ModelForm):
    
    is_agree = forms.BooleanField(error_messages={'required': 'Вы должны согласиться с Правилами и Условиями'})
    class Meta:
        model = OrganizeConferences
        fields = '__all__'

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'organization' : forms.TextInput(attrs={'class':'form-control'}),
            'org_contacts' : forms.TextInput(attrs={'class':'form-control'}),
            'org_address' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_phone(self):
        phone_len = [12, 13]
        phone = self.cleaned_data.get('phone')
        if '+998'  or '998' in phone:
            if len(phone) in phone_len:
                return phone
        raise forms.ValidationError('неправильный формат номера телефона')

    def clean_org_contacts(self):
        phone_len = [12, 13]
        org_contacts = self.cleaned_data.get('org_contacts')
        if '+998'  or '998' in org_contacts:
            if len(org_contacts) in phone_len:
                return org_contacts
        raise forms.ValidationError('неправильный формат номера телефона')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError('электронная почта недействительна')
        return email


class GrantsForm(forms.ModelForm):
    
    is_agree = forms.BooleanField(error_messages={'required': 'Вы должны согласиться с Правилами и Условиями'})
    class Meta:
        model = Grants
        fields = '__all__'

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'organization' : forms.TextInput(attrs={'class':'form-control'}),
            'org_contacts' : forms.TextInput(attrs={'class':'form-control'}),
            'org_address' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_phone(self):
        phone_len = [12, 13]
        phone = self.cleaned_data.get('phone')
        if '+998'  or '998' in phone:
            if len(phone) in phone_len:
                return phone
        raise forms.ValidationError('неправильный формат номера телефона')

    def clean_org_contacts(self):
        phone_len = [12, 13]
        org_contacts = self.cleaned_data.get('org_contacts')
        if '+998'  or '998' in org_contacts:
            if len(org_contacts) in phone_len:
                return org_contacts
        raise forms.ValidationError('неправильный формат номера телефона')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError('электронная почта недействительна')
        return email


class TranslationForm(forms.ModelForm):
    is_agree = forms.BooleanField(error_messages={'required': 'Вы должны согласиться с Правилами и Условиями'})
    class Meta:
        model = Translation
        fields = '__all__'

        widgets = {
            'word_amount' : forms.NumberInput(attrs={'class':'form-control', 'min':0}),
            'language' : forms.TextInput(attrs={'class':'form-control'}),
            'research_area' : forms.Select(attrs={'class':'form-control'}),
            'extra' : forms.Select(attrs={'class':'form-control'}),
            'comment' : forms.Textarea(attrs={'class':'form-control', 'rows':5}),
        }

        def clean_word_amount(self):
            amount = self.cleaned_data.get('word_amount')
            if amount.isdigit():
                return amount
            raise forms.ValidationError('not digit')

   


