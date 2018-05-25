# encoding=utf-8
from datetime import date, datetime
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import UserModel
userModel = UserModel()

# 为了让 JSON 支持 转 datetime 类型 （默认情况下， datetime类型不可被序列化，也就是不能转成 json字符串）
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


# Create your views here.
def index(request):
    return HttpResponse("Success")
    # 快捷写法：render()
    # return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))


def checkAllUsers(request):
    userList = userModel.findAll()
    return HttpResponse(json.dumps(userList, cls=ComplexEncoder))


@csrf_exempt
def register(request):
    if request.method == 'POST':
        userObj = json.loads(request.body)
        userModel.add(userObj)
    return HttpResponse("register success.")
    pass
