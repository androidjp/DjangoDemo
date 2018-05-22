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
