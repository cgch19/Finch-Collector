from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Finch
from .forms import FeedingForm

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

def finch_detail(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'main_app/finch_detail.html', {'finch': finch, 'feeding_form': feeding_form,})

def add_feeding(request, pk):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = pk
    new_feeding.save()
  return redirect('finch_detail', finch_id=pk)
