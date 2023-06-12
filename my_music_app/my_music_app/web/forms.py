from django import forms

from my_music_app.web.models import Profile, Album


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for name, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()
        return self.instance


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"


class AlbumCreateForm(AlbumBaseForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            'album_name': forms.TextInput(
                attrs={'placeholder': 'Album Name', }
            ),
            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist', }
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description', }
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'Image URL', }
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Price', },
            )
        }


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
