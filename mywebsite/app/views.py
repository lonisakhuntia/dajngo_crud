from django.shortcuts import render
from django.http import HttpResponse
from.models import Question_P,Choice_P

def index(request):
	latest_question=Question_P.objects.all()
	outputs="<br>".join([q.question_text for q in latest_question])
	return HttpResponse(outputs)
    #return HttpResponse("<marquee><h1><br><br><br><br>WELCOME TO MY WEBSITE!</br></br></br></br></marquee>")
def details(request,question_id):
	return HttpResponse(f'you are looking at question {question_id}')
def results(request,question_id):
	return HttpResponse(f'you are looking at results of {question_id}')
def votes(request,question_id):
	return HttpResponse(f'you are voting on question {question_id}')
	
	
