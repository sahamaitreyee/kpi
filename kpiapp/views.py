from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #mget the model
    template=loader.get_template("kpiapp/show_question.html") # load the template
    print(latest_question_list)
    context={"latest_question_list":latest_question_list} #set the context for view 
    return HttpResponse(template.render(context, request)) #invoke django MVT

def detail(request, question_id):
    try:
        options=Question.objects.get(pk=question_id)
        print(options)
    except Question.DoesNotExist:
        raise Http404("Non Existing")
    return render(request, 'kpiapp/question_choice.html',{"options":options})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'kpiapp/question_result.html', {'question': question})

def vote(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    print("Object found %s"%question)
    try:
        selected=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "kpiapp/question_choice.html", {"options":question, "error_message": "Not Selected"} )
    else:
        selected.votes+=1
        selected.save()
        return HttpResponseRedirect(reverse('kpi:result'),args=(question_id,))


