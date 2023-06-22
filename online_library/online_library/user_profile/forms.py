from django import forms

from online_library.book.models import Book
from online_library.user_profile.models import Profile


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class UserCreateForm(UserBaseForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name', }
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last Name', }
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'URL', }
            ),
        }


class UserEditForm(UserBaseForm):
    pass


class UserDeleteForm(UserBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def __set_readonly_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
            field.required = False

    def save(self, commit=True):
        if commit:
            Book.objects.all().delete()
            self.instance.delete()
        return self.instance
