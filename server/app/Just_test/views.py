from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

def index(request):

    context = {
        'num_books': 1,
        'num_instances': 2,
        'num_instances_available': 3,
        'num_authors': 4,
    }

    return render(request, 'index.html', context=context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})