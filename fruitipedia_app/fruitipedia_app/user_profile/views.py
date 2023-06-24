from django.shortcuts import render, redirect

from fruitipedia_app.fruit.models import Fruit
from fruitipedia_app.user_profile.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from fruitipedia_app.user_profile.models import Profile


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        "form": form,
    }
    return render(request, "profile/create-profile.html", context)


def profile_details(request):
    total_posts = Fruit.objects.all().count()
    context = {
        "total_posts": total_posts,
    }
    return render(request, "profile/details-profile.html", context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile_details')
    context = {
        "form": form,
        "fruit": profile,
    }
    return render(request, "profile/edit-profile.html", context)


def profile_delete(request):
    profile = Profile.objects.first()
    form = ProfileDeleteForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, "profile/delete-profile.html",context)
