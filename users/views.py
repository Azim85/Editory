from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
User = get_user_model()

class UserRegisterView(View):

    """ User Registration View """

    def get(self, request):
        form = RegisterForm()
        context = {'form':form}
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = make_password(request.POST.get('password1'))
        if form.is_valid():
            User.objects.create(first_name=first_name, email=email, phone=phone, password=password)
            return redirect('users:login')

        context = {'form':form}
        return render(request, 'users/register.html', context)


class UserLoginView(View):

    """ User Login """

    def get(self, request):
        form = LoginForm()
        context = {'form':form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'], backend='django.contrib.auth.backends.ModelBackend')
            login(request, user)
            return redirect('pages:home')
        context = {'form':form}
        return render(request, 'users/login.html', context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'home.html')





