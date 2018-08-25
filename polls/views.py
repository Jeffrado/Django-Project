from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Question


def index(request):
    # Show latest 5 question
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # load index.html
    template = loader.get_template('polls/index.html')
    # pass index.html to context
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)
    # or : HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    """
    Or can write like this:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!!")
    """
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    results_response = "You're looking alt all the result of question %s."
    return HttpResponse(results_response % question_id)

def vote(request, question_id):
    vote_response = "You're voting on question %s."
    return HttpResponse(vote_response % question_id)