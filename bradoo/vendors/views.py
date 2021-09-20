from django.shortcuts import render
from django.http import JsonResponse
from .models import Vendor
from .utils import is_valid_cnpj, get_vendor, wrong_request
from .messages import *
import json

# Create your views here.

def create(request):
    if (request.method != 'POST'):
        return JsonResponse(NOT_POST, status=405)

    name = request.POST.get("name");
    cnpj = request.POST.get("cnpj");
    city = request.POST.get("city");
    products = request.POST.get("products");
   
    if (name is None or cnpj is None):
       return JsonResponse(MISSING_REQUIRED_FIELD, status=400);
    
    if (not is_valid_cnpj(cnpj)):
        return JsonResponse(INVALID_CNPJ, status=409) 

    vendor = Vendor.objects.create(
        name = name, 
        cnpj = cnpj,
        city = city 
    )

    vendor.save()

    return JsonResponse(vendor.serialize(), status=200)

def search(request):
    if (request.method != "GET"):
        return JsonResponse(NOT_GET, status=400);

    matches = []
    name = request.GET.get("name");
    if (name is not None):
        matches = Vendor.objects.filter(name__contains=name);

    cnpj = request.GET.get("cnpj");
    
    if (cnpj is not None):
        cnpj_matches = Vendor.objects.filter(cnpj__contains=cnpj);

        if (not matches):
            matches = cnpj_matches
        else: 
            matches = [match for match in matches if match in cnpj_matches]

    matches = [match.serialize() for match in matches]

    return JsonResponse(matches, status=200, safe=False);

def update(request):
    if (request.method != "PUT"):
        return JsonResponse({"error": "Not found"}, status=400);

    body = json.loads(request.body);
    vendor = get_vendor(body);


    if (vendor is None):
        return JsonResponse({"error": "error"}, status=400);

    new_cnpj = body.get("new_CNPJ");
    new_name = body.get("new_name");

    if (new_cnpj is not None):
        if (not is_valid_cnpj(new_cnpj)):
            return JsonResponse(
        {"error": f"CNPJ '{new_cnpj}' is invalid or belongs to other account."},        status=400);
        
        vendor.update_cnpj(new_cnpj);

    if (new_name is not None):
        vendor.name = new_name;
        vendor.save(update_fields=["name"]);


    return JsonResponse(vendor.serialize(), status=200);


def delete(request):
    if (request.method != "DELETE"):
        return JsonResponse(wrong_request("DELETE", request.method), 400);

    body = json.loads(request.body);
    
    vendor = get_vendor(body);

    if (vendor is None):
        return JsonResponse({"error": "Could not find vendor matching the given data"});

    field = body.get("field");

    actions = {
        "all": Vendor.delete,
        "vendor": Vendor.delete,
        "city": Vendor.remove_city
    };

    if (field not in actions.keys()):
        return JsonResponse({"error": f"You are not allowed to delete the field {field}"}, status=403);

    
    actions[field](vendor);
    
    return JsonResponse(
            vendor.serialize() if vendor is not None else {},
            status=200);


def all(request):
    return JsonResponse({"vendors": [vendor.serialize() for vendor in Vendor.objects.all()]})



