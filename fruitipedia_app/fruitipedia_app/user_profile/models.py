from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.user_profile.validators import string_start_with_letter_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=(MinLengthValidator(2), string_start_with_letter_validator,),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=35,
        validators=(MinLengthValidator(1), string_start_with_letter_validator,),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=20,
        validators=(MinLengthValidator(8),),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        default=18,
        null=True,
        blank=True,
    )
