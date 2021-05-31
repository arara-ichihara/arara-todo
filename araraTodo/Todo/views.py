from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'Todo/index.html', 
            {'all_items':all_todo_items})

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = c)
    new_item.save()
    return HttpResponseRedirect('/todo/')
