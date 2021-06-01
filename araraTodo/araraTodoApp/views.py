from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import TodoItem

def index(request):
    todo_list = TodoItem.objects.all()
    context = {'todo_list':todo_list}
    return render(request, 'araraTodoApp/index.html', context)
