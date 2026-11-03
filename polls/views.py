from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world! You are at polls.')

def details(request,question_id):
    return HttpResponse("You'r looking at question %s" % question_id)

def results(request,question_id):
    return HttpResponse("You'r looking at result of question %s." % question_id)

def vote(request,question_id):
    return HttpResponse("You'r voting on question %s." % question_id)