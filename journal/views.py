from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Entry

# Journal views

class EntryList(ListView):
    template_name = 'journal/journal_index.html'
    model = Entry
    context_object_name = 'entries'

class CreateEntry(CreateView):
    template_name = 'journal/add_entry.html'
    model = Entry
    fields = '__all__'
    success_url = reverse_lazy('entry')

class ViewEntry(DetailView):
    template_name = 'journal/view_entry.html'
    model = Entry
    fields = '__all__'

class EditEntry(UpdateView):
    template_name = 'journal/add_entry.html'
    model = Entry
    fields = '__all__'
    success_url = reverse_lazy('entry')