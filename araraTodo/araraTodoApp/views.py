from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import TodoItem
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    todo_list = TodoItem.objects.all()
    context = {'todo_list':todo_list}
    return render(request, 'araraTodoApp/index.html', context)

def delete(request, id):
    todo = get_object_or_404(TodoItem,id=id)
    todo.delete()
    return redirect('/araraTodoApp')