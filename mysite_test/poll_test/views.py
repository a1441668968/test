from django.shortcuts import render, get_object_or_404, redirect
from .models import Question


def polls_index(request):
    # return render(request, 'polls/poll_test_index.html')
    last_question_list = Question.objects.order_by('-publish_date')[:5]
    context = {'question_list': last_question_list}
    return render(request=request, template_name='polls/poll_test_index.html', context=context)


def detail(request, q_id):
    # return render(request=request, template_name='polls/detail.html', context={'question_id': q_id})
    question = get_object_or_404(Question, id=q_id)
    return render(request=request, template_name='polls/detail.html', context={'question': question})


def result(request, q_id):
    # return render(request=request, template_name='polls/result.html', context={'question_id': q_id})
    question = get_object_or_404(Question, id=q_id)
    return render(request=request, template_name='polls/result.html', context={'question': question})


def vote(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    choice_id = request.POST.get('choice_id')
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()
    return redirect('result', q_id=q_id)  # 'result'对应urls.py中的name字段的值
