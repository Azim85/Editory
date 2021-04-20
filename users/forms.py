from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'phone')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'phone')


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'height:50px'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'height:50px'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'height:50px'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'style':'height:50px'}))
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'email', 'phone', 'password')


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'height:50px'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'style':'height:50px'}))
    