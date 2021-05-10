from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'phone', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = '__all__'


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'height:50px'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'height:50px'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'height:50px'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'style':'height:50px'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'style':'height:50px'}))
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError('электронная почта недействительна')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.startswith('+998'):
            raise forms.ValidationError('номер неправильного формата')
        return phone

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError('пароль должен состоять не менее чем из 8 символов')
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1:
            raise forms.ValidationError('пароли не совпадают')
        return password2

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        qs = get_user_model().objects.filter(phone=phone)
        if qs.exists():
            raise forms.ValidationError('этот номер телефона уже зарегистрирован')
        return phone



class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'height:50px'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'style':'height:50px'}))
    