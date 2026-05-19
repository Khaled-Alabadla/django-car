from django.urls import path
from . import views

urlpatterns = [
    path('list', views.lists, name='lists'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
]
