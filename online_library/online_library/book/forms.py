from django import forms

from online_library.book.models import Book


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Title', }
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description', }
            ),
            'image': forms.URLInput(
                attrs={'placeholder': 'Image', }
            ),
            'type': forms.TextInput(
                attrs={'placeholder': 'Fiction, Novel, Crime...', }
            ),
        }


class BookAddForm(BookBaseForm):
    pass


class BookEditForm(BookBaseForm):
    pass
