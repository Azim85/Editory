from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import OrderModel

@csrf_exempt
def check_apelsin(request):

    data = {"status":"true"}
  
    return JsonResponse(data)


def confirm_apelsin(request, pk):
    order = OrderModel.objects.get(pk=pk)
    order.payment_status = 3
    order.save()
    order.refresh_from_db()
    return redirect(request, 'users:dashboard')

