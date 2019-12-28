from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView)
from django.urls import reverse_lazy
from .models import Todo

class TodoPageViev(TemplateView):
    template_name = 'index.html'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo.html'
    fields = ['title']
    success_url = reverse_lazy('home')

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('todo')

class TodoEditView(UpdateView):
    model = Todo
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('todo')