from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, ListView
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from orders.models import OrderModel
from paymeuz.models import PaymeTransactionModel
from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import JsonResponse



import datetime
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

        context = {'form': form}
        return render(request, 'users/register.html', context)


class UserLoginView(View):

    """ User Login """

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('pages:home')
        form = LoginForm()
        context = {'form':form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'], backend='django.contrib.auth.backends.ModelBackend')
            if user is not None:
                login(request, user)
                if 'after-login' in request.session.keys():
                    return redirect(request.session['after-login'])
                if 'back-trans' in request.session.keys():
                    return redirect(request.session['back-trans'])
                
                return redirect('pages:home')
            else:
                messages.error(request, 'Email or Password is invalid')
                context = {'form':form}
                return render(request, 'users/login.html', context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'home.html')


class DasboardView(ListView):
    template_name = 'users/dashboard.html'
    context_object_name = 'orders'
    model = OrderModel
    paginate_by = 6
    ordering = ('-id',)

    def get_context_data(self, *args, **kwargs):
        context = super(DasboardView, self).get_context_data(**kwargs)
        context['form'] = ProfileForm(instance=self.request.user)
        context['user_order'] = OrderModel.objects.filter(user=self.request.user)
        context['groups'] = Group.objects.all()
        return context


    # def get(self, request):
    #     if request.user.is_authenticated:
    #         orders = OrderModel.objects.order_by('-id')[:6]
    #         user_order = OrderModel.objects.filter(user=request.user)
    #         form = ProfileForm(instance=request.user)
    #         context = {'form': form, 'orders':orders, 'user_order':user_order}
    #         return render(request, 'users/dashboard.html', context)
    #     else:
    #         return redirect('users:login')


class ProfileChange(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('users:dashboard')
    template_name = 'users/dashboard.html'


class ChangeStatusView(View):
    def get(self, request, id):
        order = OrderModel.objects.get(id=id)
        order.payment_status = 1
        order.save()
        return redirect('users:dashboard')

class ChangeStatusCashView(View):
    def get(self, request, id):
        order = OrderModel.objects.get(id=id)
        order.payment_status = 3
        order.save()
        return redirect('users:dashboard')

def check_payment(request, pk):
    order = OrderModel.objects.get( id=pk, user=request.user)
    transaction = PaymeTransactionModel.objects.get(order_id=pk)
    create_time = datetime.datetime.fromtimestamp(transaction.create_time/1000.0)
    perform_time = datetime.datetime.fromtimestamp(transaction.perform_time/1000.0)

    return render(request, 'users/check.html', {'order':order, 'transaction':transaction,
                                                'tr_id':transaction._id, 'create_time':create_time, 'perform_time':perform_time})


    


        
        

        




