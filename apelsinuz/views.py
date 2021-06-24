from apelsinuz.serializers import CallbackResponseSerializer
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import OrderModel

import json
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def check_apelsin(request):
    data = json.loads(request.body)
    serializer = CallbackResponseSerializer(data=data)
    
    if serializer.is_valid():
        data = serializer.validated_data
        if data['order_id']:
            order = OrderModel.objects.get(pk=data['order_id'])
            if order.amount == data['amount']:
                order.payment_status = 3
                order.save()
                order.refresh_from_db()
                return JsonResponse({"status": True})
        
    return JsonResponse({"status": False})


def confirm_apelsin(request, pk):
    print(pk)
    order = OrderModel.objects.get(pk=pk)
    order.payment_status = 3
    order.save()
    order.refresh_from_db()
    return redirect('users:dashboard')

