from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .forms import TaskForm
from .models import Task
from django.urls import reverse_lazy


# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class CreateTaskView(CreateView):
    template_name = "createTask.html"
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy("home")

class TodolistView(ListView):
    template_name = "list.html"
    model = Task
    context_object_name ="Task"

class TaskUpdateView(UpdateView):
    template_name = "createTask.html"
    model = Task
    form_class = TaskForm
    success_url =reverse_lazy("home")

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy("home")