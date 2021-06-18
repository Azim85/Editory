from django.shortcuts import render
from django.http import JsonResponse

def check_apelsin(request):
    data = {"status":"true"}
    return JsonResponse(data)
