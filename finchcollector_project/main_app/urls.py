from django.urls import path
from . import views
from .views import ToyDetailView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_list, name='finch_list'),
    path('finch/add/', views.FinchCreateView.as_view(), name='finch_add'),
    path('finch/<int:pk>/edit/', views.FinchUpdateView.as_view(), name='finch_edit'),
    path('finch/<int:pk>/delete/', views.FinchDeleteView.as_view(), name='finch_delete'),
    path('finch/<int:finch_id>/', views.finch_detail, name='finch_detail'),
    path('finch/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),
    # Toys
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', ToyDetailView.as_view(), name='toy_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'), 
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
