from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from . models import Todo
def index(request):
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        form=TodoForm()
        todo = Todo.objects.all()
        return render(request,'index.html',{'todo':todo,'form':form})
def delete(request, id):
        todo = Todo.objects.get(id=id)
        if request.method == 'POST':
            todo.delete()
            return redirect('index')
def update(request,id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form})                