from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.htpp import Http404
from .models import Question
from django.template import loader
# Create your views here.
# each of these functions is a view

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    #can use this render() method to accomplish the same as the other 2 commented lines
    return render(request, 'polls/index.html', context)  #takes the request object, a template name, and a dictionary. It returns an HttpResponse object of the given template rendered with the given context.
    #return HttpResponse(template.render(context,request))

def detail(request, question_id):   
    """ try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question':question}) """
    #it is common to use get() and raise Http404 if the object doesnt exist. Django provides a shortcut.
    question = get_object_or_404(Question, pk=question_id) #takes Django model as first arg, and arbitrary number of keyword arguments which it passes to get() function of the model's manager. It raises Http404 if it doesnt exist
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

