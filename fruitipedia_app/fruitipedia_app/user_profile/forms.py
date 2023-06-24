from django import forms

from fruitipedia_app.fruit.models import Fruit
from fruitipedia_app.user_profile.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email", "password"]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name', },
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last Name', }
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email', }
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Password', }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.label = ""


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "image_url", "age"]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age',
        }


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Fruit.objects.all().delete()
            self.instance.delete()
        return self.instance
