from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Task
from .forms import DescriptionForm


def welcome(request):
    return render(request, 'task_list/welcome.html', {})


def index(request):
    tasks = Task.objects.order_by('created')
    completed_tasks = Task.objects.filter(completed=True)
    form = DescriptionForm()
    if request.method == 'POST':
        form = DescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks'))
    return render(request, 'task_list/index.html', {'form': form,
                                                    'tasks': tasks,
                                                    'completed_tasks': completed_tasks})


def completed(request, task_id):
    task = Task.objects.filter(pk=task_id).update(completed=True)
    return HttpResponseRedirect(reverse('tasks'))


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('tasks'))
