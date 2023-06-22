from django.shortcuts import render, redirect

from online_library.user_profile.forms import UserCreateForm, UserEditForm, UserDeleteForm
from online_library.user_profile.models import Profile


def get_profile():
    return Profile.objects.first()


def home_page():
    profile = get_profile()
    if not profile:
        return 'common/home-no-profile.html'
    return 'common/home-with-profile.html'


def profile_create(request):
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        "form": form,
    }
    return render(request, home_page(), context)


def profile_details(request):
    return render(request, 'profile/profile.html')


def profile_edit(request):
    profile = get_profile()
    form = UserEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')
    context = {
        "form": form,
    }
    return render(request, 'profile/edit-profile.html',context)


def profile_delete(request):
    profile = get_profile()
    form = UserDeleteForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'profile/delete-profile.html', context)
