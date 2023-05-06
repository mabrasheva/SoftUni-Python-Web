from django.shortcuts import render


def register_account(request):
    return render(request, template_name='accounts/register-page.html')


def login_account(request):
    return render(request, template_name='accounts/login-page.html')


def show_account_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_account(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_account(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
