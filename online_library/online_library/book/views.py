from django.shortcuts import render, redirect

from online_library.book.forms import BookAddForm, BookEditForm
from online_library.book.models import Book


def book_add(request):
    form = BookAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'book/add-book.html', context)


def book_edit(request, pk):
    book = Book.objects.filter(pk=pk).get()
    form = BookEditForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        "form": form,
        "book": book,
    }
    return render(request, 'book/edit-book.html', context)


def book_delete(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('index')


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get()
    context = {
        "book": book,
    }
    return render(request, 'book/book-details.html', context)
