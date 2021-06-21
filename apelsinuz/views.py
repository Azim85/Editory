from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import OrderModel

@csrf_exempt
def check_apelsin(request):

    data = {"status":"false"}
    if request.POST['transactionId']:
        transaction_id = request.POST['transactionId']
        order = OrderModel.objects.get(id=transaction_id)
        order.payment_status = 3
        order.save()
        order.refresh_from_dbPOST
        data = {"status":"true"}
    return JsonResponse(data)
