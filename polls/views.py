from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = {"latest_question_list":latest_question_list}
    return render(request,'polls/index.html',output)


def details(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question do not exist")

    return render(request,'polls/details.html',{'queation':question})

def results(request,question_id):
    return HttpResponse("You'r looking at result of question %s." % question_id)

def vote(request,question_id):
    return HttpResponse("You'r voting on question %s." % question_id)