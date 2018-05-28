# encoding=utf-8
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from mongo_module.dao.dao_mongoengine import NoteDAO
from mongo_module.dao.dao_pymongo import UserDAO

userModel = UserDAO()
noteDAO = NoteDAO()


def index(request):
    return JsonResponse("Success", safe=False)


def checkAllUsers(request):
    userList = userModel.findAll()
    return JsonResponse(userList, safe=False)


def searchUser(request, user_id):
    return JsonResponse(userModel.findUserByPhoneNumOrEmail(user_id), safe=False)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        userObj = json.loads(request.body)
        userModel.add(userObj)
    return JsonResponse("register success.", safe=False)
    pass


def notes(request):
    jsonRes = {
        "code": 200,
        "data": noteDAO.findAll()
    }
    return JsonResponse(jsonRes, safe=False)


@csrf_exempt
def addNote(request):
    if request.method == 'POST':
        noteObj = json.loads(request.body)
        noteDAO.add(noteObj)
        jsonRes = {
            "code": 200,
            "message": "success"
        }
        return JsonResponse(jsonRes)
    else:
        return JsonResponse({"code": 400, "message": "Must need `POST` request."})
