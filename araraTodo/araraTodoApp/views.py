from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import TodoItem
from django.utils import timezone

def index(request):
    todo_list = TodoItem.objects.all()
    context = {'todo_list':todo_list}
    return render(request, 'araraTodoApp/index.html', context)

def addTodo(request):
    new = request.POST['content']
    new_todo_item = TodoItem(content=new, create_date=timezone.now())
    new_todo_item.save()
    return HttpResponseRedirect('/araraTodoApp/')