from django.shortcuts import render

from fruitipedia_app.fruit.models import Fruit


def index(request):
    return render(request, "common/index.html")


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        "fruits": fruits
    }
    return render(request, "common/dashboard.html", context)
