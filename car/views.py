from django.shortcuts import render

# Create your views here.

def lists(request):
  return render(request, 'car/list.html')

def add(request):
  return render(request, 'car/add.html')

def delete(request):
  return render(request, 'car/delete.html')