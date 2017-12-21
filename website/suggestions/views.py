from django.http import HttpResponse
from django.template import loader
from todolist.models import Question

def index( request ):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('suggestions/suggestions.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))