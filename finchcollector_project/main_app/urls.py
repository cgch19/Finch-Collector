from django.urls import path
from .views import FinchCreateView, FinchUpdateView, FinchDeleteView
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'), 
    path('about/', views.about, name='about'),
    path('finches/', views.finch_list, name='finch_list'),
    path('finch/add/', FinchCreateView.as_view(), name='finch_add'),
    path('finch/<int:pk>/edit/', FinchUpdateView.as_view(), name='finch_edit'),
    path('finch/<int:pk>/delete/', FinchDeleteView.as_view(), name='finch_delete'),
]