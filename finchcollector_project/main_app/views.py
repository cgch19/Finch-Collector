from django.shortcuts import render

# Create your views here.
finches = [
    {'name': 'Zebra Finch', 'scientific_name': 'Taeniopygia guttata', 'origin': 'Australia', 'colors': 'Grey, White, Black'},
    {'name': 'Gouldian Finch', 'scientific_name': 'Erythrura gouldiae', 'origin': 'Australia', 'colors': 'Red, Black, Green, Yellow'},
    {'name': 'Society Finch', 'scientific_name': 'Lonchura domestica', 'origin': 'China', 'colors': 'White, Fawn, Grey'}
]

def about(request):
    return render(request, 'main_app/about.html')

def finch_list(request):
    return render(request, 'main_app/finch_list.html', {'finches': finches})