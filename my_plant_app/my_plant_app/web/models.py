from django.db import models
from django.core.validators import MinLengthValidator

from my_plant_app.web.validators import start_with_capital_letter_validator, contain_only_letters_validator


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MIN_LEN_USERNAME = 2
    MAX_LEN_FIRST_NAME = 20
    MAX_LEN_LAST_NAME = 20

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        null=False,
        blank=False,
        validators=(MinLengthValidator(MIN_LEN_USERNAME),),
    )
    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(start_with_capital_letter_validator,),
        verbose_name="First Name",
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(start_with_capital_letter_validator,),
        verbose_name="Last Name",
        null=False,
        blank=False,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    profile_picture = models.URLField(
        verbose_name="Profile Picture",
        null=True,
        blank=True,
    )


class Plant(models.Model):
    MAX_LEN_PLANT = 14
    OUTDOOR_PLANTS = "Outdoor Plants"
    INDOOR_PLANTS = "Indoor Plants"
    PLANT_TYPES = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )
    MAX_LEN_NAME = 10
    MIN_LEN_NAME = 2

    plant_type = models.CharField(
        max_length=MAX_LEN_PLANT,
        choices=PLANT_TYPES,
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(MinLengthValidator(MIN_LEN_NAME), contain_only_letters_validator,),
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
    price = models.FloatField(
        null=False,
        blank=False,
    )
