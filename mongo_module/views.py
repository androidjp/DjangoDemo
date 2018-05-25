# encoding=utf-8
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import UserModel

userModel = UserModel()


def index(request):
    return JsonResponse("Success", safe=False)


def checkAllUsers(request):
    userList = userModel.findAll()
    return JsonResponse(userList, safe=False)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        userObj = json.loads(request.body)
        userModel.add(userObj)
    return JsonResponse("register success.", safe=False)
    pass
