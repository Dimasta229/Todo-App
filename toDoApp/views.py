from django.shortcuts import render, redirect

from toDoApp.forms import TaskModel
from .models import Todo

# Create your views here.


def index(request):
    todo = Todo.objects.all().order_by('-id')
    if request.method == 'POST':
        title = request.POST.get('title')
        form = Todo(title=title)
        form.save()
        return redirect('/')
    context = {'todos': todo}
    return render(request, 'index.html', context)


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskModel(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskModel(instance=todo)
    context = {'form': form}
    return render(request, 'update.html', context)


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
