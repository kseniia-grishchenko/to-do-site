from django.shortcuts import render

from todo.models import Task


def todo(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'todo/todo.html', {'tasks': tasks})
