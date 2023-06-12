from django.shortcuts import render, redirect

from my_music_app.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, ProfileDeleteForm
from my_music_app.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    albums = Album.objects.all()

    if not profile:
        return profile_add(request)

    context = {
        "profile": profile,
        "albums": albums,
    }
    return render(request, "core/home-with-profile.html", context)


def album_add(request):
    profile = get_profile()
    if request.method == "GET":
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, "album/add-album.html", context)


def album_details(request, pk):
    profile = get_profile()
    album = Album.objects.filter(pk=pk).get()

    context = {
        "profile": profile,
        "album": album,
    }
    return render(request, "album/album-details.html", context)


def album_edit(request, pk):
    profile = get_profile()
    album = Album.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "profile": profile,
        "album": album,
        "form": form,
    }
    return render(request, "album/edit-album.html", context)


def album_delete(request, pk):
    profile = get_profile()
    album = Album.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "profile": profile,
        "album": album,
        "form": form,
    }
    return render(request, "album/delete-album.html", context)


def profile_add(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, "core/home-no-profile.html", context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.all().count()
    context = {
        "profile": profile,
        "albums_count": albums_count,
    }
    return render(request, "profile/profile-details.html", context)


def profile_delete(request):
    profile = get_profile()

    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, "profile/profile-delete.html", context)
