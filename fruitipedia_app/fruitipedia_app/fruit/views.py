from django.shortcuts import render, redirect

from fruitipedia_app.fruit.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipedia_app.fruit.models import Fruit


def fruit_create(request):
    form = FruitCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        "form": form,
    }
    return render(request, "fruit/create-fruit.html", context)


def fruit_details(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    context = {
        "fruit": fruit,
    }
    return render(request, "fruit/details-fruit.html", context)


def fruit_edit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitEditForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
        "fruit": fruit,
    }
    return render(request, "fruit/edit-fruit.html", context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()
    form = FruitDeleteForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
        "fruit": fruit,
    }
    return render(request, "fruit/delete-fruit.html", context)
