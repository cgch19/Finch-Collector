from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), 
    path('about/', views.about, name='about'),
    path('finches/', views.finch_list, name='finch_list'),
]