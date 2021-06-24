from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import OrderModel


import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def check_apelsin(request):
    print(request.POST, request.GET)
    logger.warning(str(request.POST))
    logger.warning(str(request.GET))
    data = {"status":"true"}
  
    return JsonResponse(data)


def confirm_apelsin(request, pk):
    print(pk)
    order = OrderModel.objects.get(pk=pk)
    order.payment_status = 3
    order.save()
    order.refresh_from_db()
    return redirect('users:dashboard')

