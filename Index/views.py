from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    index_index = loader.get_template('index.html')
    context = {
        'student_name': 'dudu'
    }
    result = index_index.render(context)
    print(result)
    return HttpResponse(result)