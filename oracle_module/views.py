import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Customer


# Create your views here.

def showCustomers(request):
    customers = serializers.serialize("json", Customer.objects.all())
    customers = json.loads(customers)
    jsonRes = {
        "code": 200,
        "data": customers
    }
    return JsonResponse(jsonRes)


@csrf_exempt
def addCustomer(request):
    if request.method == 'POST':
        customer = json.loads(request.body)
        Customer.objects.create(**customer)
        jsonRes = {
            "code": 200,
            "message": "success"
        }
        return JsonResponse(jsonRes)
    else:
        return JsonResponse({"code": 400, "message": "Must need `POST` request."})
