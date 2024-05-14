from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Finch, Toy
from .forms import FeedingForm

# Add ToyList and ToyCreate views
class ToyList(ListView):
    model = Toy
    template_name = 'main_app/toy_list.html'
    context_object_name = 'toys'

class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']
    template_name = 'main_app/toy_create.html'
    success_url = '/toys/'

class ToyDetailView(DetailView):
    model = Toy
    template_name = 'main_app/toy_detail.html'  # Replace with the actual template name for toy details
    context_object_name = 'toy'

# Add ToyUpdate view
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']
    template_name = 'main_app/toy_form.html'  # Reuse the same form template
    success_url = reverse_lazy('toys_index')  # Adjust the success URL as needed

# Add ToyDelete view
class ToyDelete(DeleteView):
    model = Toy
    template_name = 'main_app/toy_confirm_delete.html'  # Specify the delete confirmation template
    success_url = reverse_lazy('toys_index')  # Adjust the success URL as needed

# Toy list view
def toy_list(request, finch_id=None):
    toys = Toy.objects.all()  # By default, fetch all toys
    if finch_id:
        toys = toys.filter(finch_id=finch_id)  # Filter toys by the specified finch ID
    return render(request, 'main_app/toy_list.html', {'toys': toys})

# Below are the existing views you provided
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
    toys = Toy
    # Get the toys the cat doesn't have...
    # First, create a list of the toy ids that the cat DOES have
    id_list = finch.toys.all().values_list('id')
    # Now we can query for toys whose ids are not in the list using exclude
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    return render(request, 'main_app/finch_detail.html', {'finch': finch, 'feeding_form': feeding_form,'toys': toys_finch_doesnt_have})

def add_feeding(request, pk):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = pk
        new_feeding.save()
    return redirect('finch_detail', finch_id=pk)

def assoc_toy(request, pk, toy_pk):
  Finch.objects.get(id=pk).toys.add(toy_pk)
  return redirect('finch_detail', finch_id=pk)
