from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.fruit.validators import string_contain_only_letter_validator


class Fruit(models.Model):
    name = models.CharField(
        max_length=25,
        validators=(MinLengthValidator(2), string_contain_only_letter_validator,),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )
