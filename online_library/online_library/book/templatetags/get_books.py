from django import template

from online_library.book.models import Book

register = template.Library()


@register.simple_tag
def get_all_books():
    return Book.objects.all()


