from django import forms

from my_plant_app.web.models import Profile, Plant


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class ProfileCreateForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class ProfileEditForm(BaseProfileForm):
    pass


class ProfileDeleteForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            self.instance.delete()
        return self.instance


class PlantCreateForm(BasePlantForm):
    pass


class PlantEditForm(BasePlantForm):
    pass


class PlantDeleteForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
