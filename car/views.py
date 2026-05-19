from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Car
from .forms import CarForm


def lists(request):
  q = request.GET.get('q', '')
  cars = Car.objects.all().order_by('-id')
  if q:
    cars = cars.filter(brand__icontains=q)

  paginator = Paginator(cars, 10)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  context = {
    'cars': page_obj,
    'q': q,
    'page_obj': page_obj,
  }
  return render(request, 'car/list.html', context)


def add(request):
  if request.method == 'POST':
    form = CarForm(request.POST)
    if form.is_valid():
      car = form.save()
      messages.success(request, f'Car "{car.brand} ({car.year})" added.')
      return redirect(reverse('lists'))
  else:
    form = CarForm()

  return render(request, 'car/add.html', {'form': form})


def edit(request, pk):
  car = get_object_or_404(Car, pk=pk)
  if request.method == 'POST':
    form = CarForm(request.POST, instance=car)
    if form.is_valid():
      form.save()
      messages.success(request, 'Car updated successfully.')
      return redirect(reverse('lists'))
  else:
    form = CarForm(instance=car)
  return render(request, 'car/add.html', {'form': form, 'car': car})


def delete(request, pk):
    # deletion is only allowed via POST from the list page
    if request.method == 'POST':
        car = get_object_or_404(Car, pk=pk)
        car.delete()
        messages.success(request, 'Car deleted.')
    return redirect(reverse('lists'))