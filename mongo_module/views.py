from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Success")
    # 快捷写法：render()
    # return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
