from django.shortcuts import render


def index(request):
    return render(request, template_name='common/home-page.html')
