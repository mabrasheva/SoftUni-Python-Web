from django import forms

from fruitipedia_app.fruit.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"


class FruitCreateForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Fruit Name', },
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'Fruit Image URL', }
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Fruit Description', }
            ),
            'nutrition': forms.Textarea(
                attrs={'placeholder': 'Nutrition Info', }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.label = ""


class FruitEditForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }


class FruitDeleteForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = ["name", "image_url", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
