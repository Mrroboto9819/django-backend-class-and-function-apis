from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.views import generic


## Class views

class IndexView(generic.ListView):
    template_name = "questions/index.html"
    context_object_name = "question_list"

    def get_queryset(self):
        """ Retunr last five questions """
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DeleteView):
    model = Question
    template_name = "questions/detail.html"
    context_object_name = "question"
    
class ResultView(generic.DeleteView):
    model = Question
    template_name = "questions/results.html"
    context_object_name = "question"

## Function Views

# def index(request):
#     lastes_question_list = Question.objects.all()
#     return render(request, "questions/index.html", {
#         "question_list": lastes_question_list
#     })

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "questions/detail.html", {
#         "question": question
#     })

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "questions/results.html", {
#         "question": question
#     })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "questions/detail.html", {
            "question" : question,
            "error_message": "Ups... error saving the answer"
        })
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("test:results", args=[question.id]))


