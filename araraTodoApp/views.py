from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import TodoItem

from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    todo_list = TodoItem.objects.all()
    context = {'todo_list':todo_list}
    return render(request, 'araraTodoApp/index.html', context)

def addTodo(request):
    new = request.POST['content']
    new_todo_item = TodoItem(content=new, create_date=timezone.now())
    new_todo_item.save()
    return HttpResponseRedirect('/araraTodoApp/')
def delete(request, id):
    todo = get_object_or_404(TodoItem,id=id)
    todo.delete()
    return redirect('/araraTodoApp')
def update(request, id):
    todo = get_object_or_404(TodoItem,id=id)
    if content := request.POST["content_up"]:
        todo.content = content
    todo.full_clean()
    todo.save()
    return redirect('/araraTodoApp')
