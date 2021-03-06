from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


# Create your views here.


def index(request):
    # polls/
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = '. '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list
    }
    # 快捷写法：render()
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))


# 原始写法
# def index(request):
#     # polls/
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = '. '.join([q.question_text for q in latest_question_list])
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # try:
    # 更快的写法
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def say520(request, words):
    print(request.path)
    print(words)
    # words = request.read('words')
    return HttpResponse(simpleLove(words))


def buildContent(words):
    res = ''
    for item in words.split():
        # 要想实现打印出字符间的空格效果，此处添加：item = item+' '
        letterlist = []  # letterlist是所有打印字符的总list，里面包含y条子列表list_X
        for y in range(12, -12, -1):
            list_X = []  # list_X是X轴上的打印字符列表，里面装着一个String类的letters
            letters = ''  # letters即为list_X内的字符串，实际是本行要打印的所有字符
            for x in range(-30, 30):  # *是乘法，**是幂次方
                expression = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
                if expression <= 0:
                    letters += item[(x - y) % len(item)]
                else:
                    letters += ' '
            list_X.append(letters)
            letterlist += list_X
        print('\n'.join(letterlist))
        res += '<p>'.join(letterlist).join('</p>')
        # time.sleep(1.5)
    return res


def simpleLove(words):
    if words is None:
        return
    size = len(words)
    res = '\n'.join([''.join([(words[(x - y) % size] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
            x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)])
    print(res)
    res = res.replace(' ', '&nbsp;')
    res = res.replace('\n', '<br>')
    return res