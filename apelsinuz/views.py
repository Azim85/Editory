from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def check_apelsin(request):
    data = {"status":"true"}
    return JsonResponse(data)
