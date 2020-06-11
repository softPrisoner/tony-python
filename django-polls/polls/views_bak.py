from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
# from django.http import Http404
from django.urls import reverse


def index(request):

    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template("polls/index.html")
    context = {'latest_question_list': latest_question_list}
    # template render the view
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


# detail mock
def detail(request, question_id):
   # try:
    question = get_object_or_404(Question, pk=question_id)
   # except Exception:
    # raise Http404("Question does't not exist")
    return render(request, "polls/detail.html", {"question": question})
# return HttpResponse("You're looking at question %s" % question_id)
# result mock


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
    # return HttpResponse(response % question_id)

# vote mock


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Exception):
        return render(request, "polls/details.html", {"question": question, "error_message": "you didn't choose anyone"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return HttpResponse("you are voting on question.%s " % question_id)
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
