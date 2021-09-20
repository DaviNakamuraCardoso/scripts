from django.shortcuts import render
from django.http import JsonResponse
from vendors.utils import wrong_request 
from .models import Product
from .utils import get_product

# Create your views here.
def all(request):
    return JsonResponse({
        "products": 
        [product.serialize() for product in Product.objects.all()]})


def create(request):
    if (request.method != "POST"):
        return JsonResponse(wrong_method("POST", request.method), status=400);


def search(request):
    if (request.method != "GET"):
        return JsonResponse(wrong_method("GET", request.method), status=400);

def update(request):
    if (request.method != "PUT"):
        return JsonResponse(wrong_method("PUT", request.method), status=400);

def delete(request):
    if (request.method != "DELETE"):
        return JsonResponse(wrong_method("DELETE", request.method), status=400);

    

