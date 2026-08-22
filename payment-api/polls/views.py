from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import Http404

def index( request ):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list" : latest_question_list}
    return render(request, "polls/index.html", context)

def contact( request ):
    return HttpResponse("You're in the Contact page of the polls.")

def detail(request, question_id):
    # try :
    question = get_object_or_404( Question, pk=question_id)
    # except:
    #     raise Http404("Question does not exist")
    return render(request, "polls/details.html", {"question" : question})

def results(request, question_id):
    response = "You're looking at the results of the questions: %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're looking at the votes of the questions: %s." % question_id)