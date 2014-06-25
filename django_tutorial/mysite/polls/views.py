import django.shortcuts
# Create your views here.
from polls.models import Question
import django.http

def index(request):
    latest_poll_list = Question.objects.order_by("-pub_date")[:5]
    context={'latest_poll_list':latest_poll_list}
    return django.shortcuts.render(request, 'polls/index.html', context)

def detail(request, poll_id):
    question = django.shortcuts.get_object_or_404(Question,pk=poll_id)
    return django.shortcuts.render(request, 'polls/detail.html', {'question':question})

def results(request, poll_id):
    return django.http.HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return django.http.HttpResponse("You're voting on poll %s." % poll_id)
