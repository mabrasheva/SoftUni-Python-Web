from django.shortcuts import render

from petstagram.photos.models import Photo


def add_photo(request):
    return render(request, template_name='photos/photo-add-page.html')


def edit_photo(request, pk):
    return render(request, template_name='photos/photo-edit-page.html')


def show_photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
    }
    return render(request, template_name='photos/photo-details-page.html', context=context)


def delete_photo(request, pk):
    return None
