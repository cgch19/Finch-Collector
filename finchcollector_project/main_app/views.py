from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Finch, Feeding

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
    feedings = Feeding.objects.filter(finch=finch)
    return render(request, 'main_app/finch_detail.html', {'finch': finch, 'feedings': feedings})

def add_feeding(request, finch_id):
    if request.method == 'POST':
        finch = get_object_or_404(Finch, pk=finch_id)

        date = request.POST.get('date')
        food_type = request.POST.get('food_type')
        food_amount = request.POST.get('food_amount')
        feeding = Feeding.objects.create(finch=finch, date=date, food_type=food_type, food_amount=food_amount)
        return redirect('finch_detail', finch_id=finch_id)
