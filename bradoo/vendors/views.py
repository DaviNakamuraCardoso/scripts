from django.shortcuts import render
from django.http import JsonResponse
from .models import Vendor
from .utils import is_valid_cnpj
from .messages import NOT_POST, INVALID_CNPJ

# Create your views here.

def create(request):
    if (request.method != 'POST'):
        return JsonResponse(NOT_POST, status=405)

    name = request.POST['name']
    cnpj = request.POST['cnpj']
    
    if (not is_valid_cnpj(cnpj)):
        return JsonResponse(INVALID_CNPJ, status=409) 

    vendor = Vendor.objects.create(
        name = name, 
        cnpj = cnpj,
        city = city
    )

    vendor.save()

    return JsonResponse(vendor.serialize(), status=200)


def all(request):
    return JsonResponse({"vendors": [vendor.serialize() for vendor in Vendor.objects.all()]})


