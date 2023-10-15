from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

"""
Методы обрабатывают логику работы страниц - index - главная страница, 
create - добавление записи, about - страница об авторе.
"""


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def about(request):
    return render(request, 'main/about.html')


"""
Простой пример
# def about(request):
#     return HttpResponse("<h4>About</h4>")
"""
