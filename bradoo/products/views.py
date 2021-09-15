from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

# Create your views here.
def all(request):
    return JsonResponse({
        "products": 
        [product.serialize() for product in Product.objects.all()]})



