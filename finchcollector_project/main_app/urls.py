from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_list, name='finch_list'),
    path('finch/add/', views.FinchCreateView.as_view(), name='finch_add'),
    path('finch/<int:pk>/edit/', views.FinchUpdateView.as_view(), name='finch_edit'),
    path('finch/<int:pk>/delete/', views.FinchDeleteView.as_view(), name='finch_delete'),
    path('finch/<int:finch_id>/', views.finch_detail, name='finch_detail'),
    path('finch/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]
