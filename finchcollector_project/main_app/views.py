from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Finch
from django.urls import reverse_lazy

def homepage(request):
    return render(request, 'main_app/homepage.html')

def about(request):
    return render(request, 'main_app/about.html')

def finch_list(request):
    finches = Finch.objects.all()
    return render(request, 'main_app/finch_list.html', {'finches': finches})

class FinchCreateView(CreateView):
    model = Finch
    fields = ['name', 'scientific_name', 'origin', 'colors']
    success_url = reverse_lazy('finch_list')
    template_name = 'main_app/finch_form.html'

class FinchUpdateView(UpdateView):
    model = Finch
    fields = ['name', 'scientific_name', 'origin', 'colors']
    template_name = 'main_app/finch_edit.html'  
    success_url = reverse_lazy('finch_list') 

class FinchDeleteView(DeleteView):
    model = Finch
    success_url = reverse_lazy('finch_list')
    template_name = 'main_app/finch_confirm_delete.html'
