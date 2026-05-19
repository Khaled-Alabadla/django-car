from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists, name='lists'),
    path('list', views.lists, name='lists'),
    path('add', views.add, name='add'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
